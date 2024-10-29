import { isArray, isNumber, isObject } from 'vega-util';
import { isBinning } from '../../bin';
import { ANGLE, COLOR, FILL, FILLOPACITY, getOffsetScaleChannel, getSizeChannel, isXorY, isXorYOffset, OPACITY, RADIUS, SCALE_CHANNELS, SHAPE, SIZE, STROKE, STROKEDASH, STROKEOPACITY, STROKEWIDTH, THETA, X, XOFFSET, Y, YOFFSET } from '../../channel';
import { getFieldOrDatumDef, isFieldOrDatumDef } from '../../channeldef';
import { getViewConfigDiscreteSize, getViewConfigDiscreteStep } from '../../config';
import { DataSourceType } from '../../data';
import { channelHasFieldOrDatum } from '../../encoding';
import * as log from '../../log';
import { channelScalePropertyIncompatability, hasContinuousDomain, hasDiscreteDomain, isContinuousToDiscrete, isExtendedScheme, scaleTypeSupportProperty } from '../../scale';
import { getStepFor, isStep } from '../../spec/base';
import { isDiscrete } from '../../type';
import * as util from '../../util';
import { isSignalRef } from '../../vega.schema';
import { exprFromSignalRefOrValue, signalOrStringValue } from '../common';
import { getBinSignalName } from '../data/bin';
import { SignalRefWrapper } from '../signal';
import { makeExplicit, makeImplicit } from '../split';
export const RANGE_PROPERTIES = ['range', 'scheme'];
export function parseUnitScaleRange(model) {
    const localScaleComponents = model.component.scales;
    // use SCALE_CHANNELS instead of scales[channel] to ensure that x, y come first!
    for (const channel of SCALE_CHANNELS) {
        const localScaleCmpt = localScaleComponents[channel];
        if (!localScaleCmpt) {
            continue;
        }
        const rangeWithExplicit = parseRangeForChannel(channel, model);
        localScaleCmpt.setWithExplicit('range', rangeWithExplicit);
    }
}
function getBinStepSignal(model, channel) {
    const fieldDef = model.fieldDef(channel);
    if (fieldDef === null || fieldDef === void 0 ? void 0 : fieldDef.bin) {
        const { bin, field } = fieldDef;
        const sizeType = getSizeChannel(channel);
        const sizeSignal = model.getName(sizeType);
        if (isObject(bin) && bin.binned && bin.step !== undefined) {
            return new SignalRefWrapper(() => {
                const scaleName = model.scaleName(channel);
                const binCount = `(domain("${scaleName}")[1] - domain("${scaleName}")[0]) / ${bin.step}`;
                return `${model.getSignalName(sizeSignal)} / (${binCount})`;
            });
        }
        else if (isBinning(bin)) {
            const binSignal = getBinSignalName(model, field, bin);
            // TODO: extract this to be range step signal
            return new SignalRefWrapper(() => {
                const updatedName = model.getSignalName(binSignal);
                const binCount = `(${updatedName}.stop - ${updatedName}.start) / ${updatedName}.step`;
                return `${model.getSignalName(sizeSignal)} / (${binCount})`;
            });
        }
    }
    return undefined;
}
/**
 * Return mixins that includes one of the Vega range types (explicit range, range.step, range.scheme).
 */
export function parseRangeForChannel(channel, model) {
    const specifiedScale = model.specifiedScales[channel];
    const { size } = model;
    const mergedScaleCmpt = model.getScaleComponent(channel);
    const scaleType = mergedScaleCmpt.get('type');
    // Check if any of the range properties is specified.
    // If so, check if it is compatible and make sure that we only output one of the properties
    for (const property of RANGE_PROPERTIES) {
        if (specifiedScale[property] !== undefined) {
            const supportedByScaleType = scaleTypeSupportProperty(scaleType, property);
            const channelIncompatability = channelScalePropertyIncompatability(channel, property);
            if (!supportedByScaleType) {
                log.warn(log.message.scalePropertyNotWorkWithScaleType(scaleType, property, channel));
            }
            else if (channelIncompatability) {
                // channel
                log.warn(channelIncompatability);
            }
            else {
                switch (property) {
                    case 'range': {
                        const range = specifiedScale.range;
                        if (isArray(range)) {
                            if (isXorY(channel)) {
                                return makeExplicit(range.map(v => {
                                    if (v === 'width' || v === 'height') {
                                        // get signal for width/height
                                        // Just like default range logic below, we use SignalRefWrapper to account for potential merges and renames.
                                        const sizeSignal = model.getName(v);
                                        const getSignalName = model.getSignalName.bind(model);
                                        return SignalRefWrapper.fromName(getSignalName, sizeSignal);
                                    }
                                    return v;
                                }));
                            }
                        }
                        else if (isObject(range)) {
                            return makeExplicit({
                                data: model.requestDataName(DataSourceType.Main),
                                field: range.field,
                                sort: { op: 'min', field: model.vgField(channel) }
                            });
                        }
                        return makeExplicit(range);
                    }
                    case 'scheme':
                        return makeExplicit(parseScheme(specifiedScale[property]));
                }
            }
        }
    }
    const sizeChannel = channel === X || channel === 'xOffset' ? 'width' : 'height';
    const sizeValue = size[sizeChannel];
    if (isStep(sizeValue)) {
        if (isXorY(channel)) {
            if (hasDiscreteDomain(scaleType)) {
                const step = getPositionStep(sizeValue, model, channel);
                // Need to be explicit so layer with step wins over layer without step
                if (step) {
                    return makeExplicit({ step });
                }
            }
            else {
                log.warn(log.message.stepDropped(sizeChannel));
            }
        }
        else if (isXorYOffset(channel)) {
            const positionChannel = channel === XOFFSET ? 'x' : 'y';
            const positionScaleCmpt = model.getScaleComponent(positionChannel);
            const positionScaleType = positionScaleCmpt.get('type');
            if (positionScaleType === 'band') {
                const step = getOffsetStep(sizeValue, scaleType);
                if (step) {
                    return makeExplicit(step);
                }
            }
        }
    }
    const { rangeMin, rangeMax } = specifiedScale;
    const d = defaultRange(channel, model);
    if ((rangeMin !== undefined || rangeMax !== undefined) &&
        // it's ok to check just rangeMin's compatibility since rangeMin/rangeMax are the same
        scaleTypeSupportProperty(scaleType, 'rangeMin') &&
        isArray(d) &&
        d.length === 2) {
        return makeExplicit([rangeMin !== null && rangeMin !== void 0 ? rangeMin : d[0], rangeMax !== null && rangeMax !== void 0 ? rangeMax : d[1]]);
    }
    return makeImplicit(d);
}
function parseScheme(scheme) {
    if (isExtendedScheme(scheme)) {
        return Object.assign({ scheme: scheme.name }, util.omit(scheme, ['name']));
    }
    return { scheme };
}
function defaultRange(channel, model) {
    const { size, config, mark, encoding } = model;
    const getSignalName = model.getSignalName.bind(model);
    const { type } = getFieldOrDatumDef(encoding[channel]);
    const mergedScaleCmpt = model.getScaleComponent(channel);
    const scaleType = mergedScaleCmpt.get('type');
    const { domain, domainMid } = model.specifiedScales[channel];
    switch (channel) {
        case X:
        case Y: {
            // If there is no explicit width/height for discrete x/y scales
            if (util.contains(['point', 'band'], scaleType)) {
                const positionSize = getDiscretePositionSize(channel, size, config.view);
                if (isStep(positionSize)) {
                    const step = getPositionStep(positionSize, model, channel);
                    return { step };
                }
            }
            // If step is null, use zero to width or height.
            // Note that we use SignalRefWrapper to account for potential merges and renames.
            const sizeType = getSizeChannel(channel);
            const sizeSignal = model.getName(sizeType);
            if (channel === Y && hasContinuousDomain(scaleType)) {
                // For y continuous scale, we have to start from the height as the bottom part has the max value.
                return [SignalRefWrapper.fromName(getSignalName, sizeSignal), 0];
            }
            else {
                return [0, SignalRefWrapper.fromName(getSignalName, sizeSignal)];
            }
        }
        case XOFFSET:
        case YOFFSET:
            return getOffsetRange(channel, model, scaleType);
        case SIZE: {
            // TODO: support custom rangeMin, rangeMax
            const zero = model.component.scales[channel].get('zero');
            const rangeMin = sizeRangeMin(mark, zero, config);
            const rangeMax = sizeRangeMax(mark, size, model, config);
            if (isContinuousToDiscrete(scaleType)) {
                return interpolateRange(rangeMin, rangeMax, defaultContinuousToDiscreteCount(scaleType, config, domain, channel));
            }
            else {
                return [rangeMin, rangeMax];
            }
        }
        case THETA:
            return [0, Math.PI * 2];
        case ANGLE:
            // TODO: add config.scale.min/maxAngleDegree (for point and text) and config.scale.min/maxAngleRadian (for arc) once we add arc marks.
            // (It's weird to add just config.scale.min/maxAngleDegree for now)
            return [0, 360];
        case RADIUS: {
            // max radius = half od min(width,height)
            return [
                0,
                new SignalRefWrapper(() => {
                    const w = model.getSignalName('width');
                    const h = model.getSignalName('height');
                    return `min(${w},${h})/2`;
                })
            ];
        }
        case STROKEWIDTH:
            // TODO: support custom rangeMin, rangeMax
            return [config.scale.minStrokeWidth, config.scale.maxStrokeWidth];
        case STROKEDASH:
            return [
                // TODO: add this to Vega's config.range?
                [1, 0],
                [4, 2],
                [2, 1],
                [1, 1],
                [1, 2, 4, 2]
            ];
        case SHAPE:
            return 'symbol';
        case COLOR:
        case FILL:
        case STROKE:
            if (scaleType === 'ordinal') {
                // Only nominal data uses ordinal scale by default
                return type === 'nominal' ? 'category' : 'ordinal';
            }
            else {
                if (domainMid !== undefined) {
                    return 'diverging';
                }
                else {
                    return mark === 'rect' || mark === 'geoshape' ? 'heatmap' : 'ramp';
                }
            }
        case OPACITY:
        case FILLOPACITY:
        case STROKEOPACITY:
            // TODO: support custom rangeMin, rangeMax
            return [config.scale.minOpacity, config.scale.maxOpacity];
    }
}
function getPositionStep(step, model, channel) {
    var _a, _b, _c, _d, _e;
    const { encoding } = model;
    const mergedScaleCmpt = model.getScaleComponent(channel);
    const offsetChannel = getOffsetScaleChannel(channel);
    const offsetDef = encoding[offsetChannel];
    const stepFor = getStepFor({ step, offsetIsDiscrete: isFieldOrDatumDef(offsetDef) && isDiscrete(offsetDef.type) });
    if (stepFor === 'offset' && channelHasFieldOrDatum(encoding, offsetChannel)) {
        const offsetScaleCmpt = model.getScaleComponent(offsetChannel);
        const offsetScaleName = model.scaleName(offsetChannel);
        let stepCount = `domain('${offsetScaleName}').length`;
        if (offsetScaleCmpt.get('type') === 'band') {
            const offsetPaddingInner = (_b = (_a = offsetScaleCmpt.get('paddingInner')) !== null && _a !== void 0 ? _a : offsetScaleCmpt.get('padding')) !== null && _b !== void 0 ? _b : 0;
            const offsetPaddingOuter = (_d = (_c = offsetScaleCmpt.get('paddingOuter')) !== null && _c !== void 0 ? _c : offsetScaleCmpt.get('padding')) !== null && _d !== void 0 ? _d : 0;
            stepCount = `bandspace(${stepCount}, ${offsetPaddingInner}, ${offsetPaddingOuter})`;
        }
        const paddingInner = (_e = mergedScaleCmpt.get('paddingInner')) !== null && _e !== void 0 ? _e : mergedScaleCmpt.get('padding');
        return {
            signal: `${step.step} * ${stepCount} / (1-${exprFromSignalRefOrValue(paddingInner)})`
        };
    }
    else {
        return step.step;
    }
}
function getOffsetStep(step, offsetScaleType) {
    const stepFor = getStepFor({ step, offsetIsDiscrete: hasDiscreteDomain(offsetScaleType) });
    if (stepFor === 'offset') {
        return { step: step.step };
    }
    return undefined;
}
function getOffsetRange(channel, model, offsetScaleType) {
    const positionChannel = channel === XOFFSET ? 'x' : 'y';
    const positionScaleCmpt = model.getScaleComponent(positionChannel);
    const positionScaleType = positionScaleCmpt.get('type');
    const positionScaleName = model.scaleName(positionChannel);
    if (positionScaleType === 'band') {
        const size = getDiscretePositionSize(positionChannel, model.size, model.config.view);
        if (isStep(size)) {
            // step is for offset
            const step = getOffsetStep(size, offsetScaleType);
            if (step) {
                return step;
            }
        }
        // otherwise use the position
        return [0, { signal: `bandwidth('${positionScaleName}')` }];
    }
    else {
        // continuous scale
        return util.never(`Cannot use ${channel} scale if ${positionChannel} scale is not discrete.`);
    }
}
function getDiscretePositionSize(channel, size, viewConfig) {
    const sizeChannel = channel === X ? 'width' : 'height';
    const sizeValue = size[sizeChannel];
    if (sizeValue) {
        return sizeValue;
    }
    return getViewConfigDiscreteSize(viewConfig, sizeChannel);
}
export function defaultContinuousToDiscreteCount(scaleType, config, domain, channel) {
    switch (scaleType) {
        case 'quantile':
            return config.scale.quantileCount;
        case 'quantize':
            return config.scale.quantizeCount;
        case 'threshold':
            if (domain !== undefined && isArray(domain)) {
                return domain.length + 1;
            }
            else {
                log.warn(log.message.domainRequiredForThresholdScale(channel));
                // default threshold boundaries for threshold scale since domain has cardinality of 2
                return 3;
            }
    }
}
/**
 * Returns the linear interpolation of the range according to the cardinality
 *
 * @param rangeMin start of the range
 * @param rangeMax end of the range
 * @param cardinality number of values in the output range
 */
export function interpolateRange(rangeMin, rangeMax, cardinality) {
    // always return a signal since it's better to compute the sequence in Vega later
    const f = () => {
        const rMax = signalOrStringValue(rangeMax);
        const rMin = signalOrStringValue(rangeMin);
        const step = `(${rMax} - ${rMin}) / (${cardinality} - 1)`;
        return `sequence(${rMin}, ${rMax} + ${step}, ${step})`;
    };
    if (isSignalRef(rangeMax)) {
        return new SignalRefWrapper(f);
    }
    else {
        return { signal: f() };
    }
}
function sizeRangeMin(mark, zero, config) {
    if (zero) {
        if (isSignalRef(zero)) {
            return { signal: `${zero.signal} ? 0 : ${sizeRangeMin(mark, false, config)}` };
        }
        else {
            return 0;
        }
    }
    switch (mark) {
        case 'bar':
        case 'tick':
            return config.scale.minBandSize;
        case 'line':
        case 'trail':
        case 'rule':
            return config.scale.minStrokeWidth;
        case 'text':
            return config.scale.minFontSize;
        case 'point':
        case 'square':
        case 'circle':
            return config.scale.minSize;
    }
    /* istanbul ignore next: should never reach here */
    // sizeRangeMin not implemented for the mark
    throw new Error(log.message.incompatibleChannel('size', mark));
}
export const MAX_SIZE_RANGE_STEP_RATIO = 0.95;
function sizeRangeMax(mark, size, model, config) {
    const xyStepSignals = {
        x: getBinStepSignal(model, 'x'),
        y: getBinStepSignal(model, 'y')
    };
    switch (mark) {
        case 'bar':
        case 'tick': {
            if (config.scale.maxBandSize !== undefined) {
                return config.scale.maxBandSize;
            }
            const min = minXYStep(size, xyStepSignals, config.view);
            if (isNumber(min)) {
                return min - 1;
            }
            else {
                return new SignalRefWrapper(() => `${min.signal} - 1`);
            }
        }
        case 'line':
        case 'trail':
        case 'rule':
            return config.scale.maxStrokeWidth;
        case 'text':
            return config.scale.maxFontSize;
        case 'point':
        case 'square':
        case 'circle': {
            if (config.scale.maxSize) {
                return config.scale.maxSize;
            }
            const pointStep = minXYStep(size, xyStepSignals, config.view);
            if (isNumber(pointStep)) {
                return Math.pow(MAX_SIZE_RANGE_STEP_RATIO * pointStep, 2);
            }
            else {
                return new SignalRefWrapper(() => `pow(${MAX_SIZE_RANGE_STEP_RATIO} * ${pointStep.signal}, 2)`);
            }
        }
    }
    /* istanbul ignore next: should never reach here */
    // sizeRangeMax not implemented for the mark
    throw new Error(log.message.incompatibleChannel('size', mark));
}
/**
 * @returns {number} Range step of x or y or minimum between the two if both are ordinal scale.
 */
function minXYStep(size, xyStepSignals, viewConfig) {
    const widthStep = isStep(size.width) ? size.width.step : getViewConfigDiscreteStep(viewConfig, 'width');
    const heightStep = isStep(size.height) ? size.height.step : getViewConfigDiscreteStep(viewConfig, 'height');
    if (xyStepSignals.x || xyStepSignals.y) {
        return new SignalRefWrapper(() => {
            const exprs = [
                xyStepSignals.x ? xyStepSignals.x.signal : widthStep,
                xyStepSignals.y ? xyStepSignals.y.signal : heightStep
            ];
            return `min(${exprs.join(', ')})`;
        });
    }
    return Math.min(widthStep, heightStep);
}
//# sourceMappingURL=range.js.map