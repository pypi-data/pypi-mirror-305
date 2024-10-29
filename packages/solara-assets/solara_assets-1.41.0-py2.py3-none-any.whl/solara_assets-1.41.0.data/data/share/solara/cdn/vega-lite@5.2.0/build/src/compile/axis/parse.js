import { AXIS_PARTS, isAxisProperty, isConditionalAxisValue } from '../../axis';
import { POSITION_SCALE_CHANNELS } from '../../channel';
import { getFieldOrDatumDef } from '../../channeldef';
import { getFirstDefined, isEmpty, keys, normalizeAngle } from '../../util';
import { isSignalRef } from '../../vega.schema';
import { mergeTitleComponent } from '../common';
import { guideEncodeEntry } from '../guide';
import { parseGuideResolve } from '../resolve';
import { defaultTieBreaker, mergeValuesWithExplicit } from '../split';
import { AxisComponent, AXIS_COMPONENT_PROPERTIES } from './component';
import { getAxisConfig, getAxisConfigs } from './config';
import * as encode from './encode';
import { axisRules, defaultOrient, getFieldDefTitle, getLabelAngle } from './properties';
export function parseUnitAxes(model) {
    return POSITION_SCALE_CHANNELS.reduce((axis, channel) => {
        if (model.component.scales[channel]) {
            axis[channel] = [parseAxis(channel, model)];
        }
        return axis;
    }, {});
}
const OPPOSITE_ORIENT = {
    bottom: 'top',
    top: 'bottom',
    left: 'right',
    right: 'left'
};
export function parseLayerAxes(model) {
    var _a;
    const { axes, resolve } = model.component;
    const axisCount = { top: 0, bottom: 0, right: 0, left: 0 };
    for (const child of model.children) {
        child.parseAxesAndHeaders();
        for (const channel of keys(child.component.axes)) {
            resolve.axis[channel] = parseGuideResolve(model.component.resolve, channel);
            if (resolve.axis[channel] === 'shared') {
                // If the resolve says shared (and has not been overridden)
                // We will try to merge and see if there is a conflict
                axes[channel] = mergeAxisComponents(axes[channel], child.component.axes[channel]);
                if (!axes[channel]) {
                    // If merge returns nothing, there is a conflict so we cannot make the axis shared.
                    // Thus, mark axis as independent and remove the axis component.
                    resolve.axis[channel] = 'independent';
                    delete axes[channel];
                }
            }
        }
    }
    // Move axes to layer's axis component and merge shared axes
    for (const channel of POSITION_SCALE_CHANNELS) {
        for (const child of model.children) {
            if (!child.component.axes[channel]) {
                // skip if the child does not have a particular axis
                continue;
            }
            if (resolve.axis[channel] === 'independent') {
                // If axes are independent, concat the axisComponent array.
                axes[channel] = ((_a = axes[channel]) !== null && _a !== void 0 ? _a : []).concat(child.component.axes[channel]);
                // Automatically adjust orient
                for (const axisComponent of child.component.axes[channel]) {
                    const { value: orient, explicit } = axisComponent.getWithExplicit('orient');
                    if (isSignalRef(orient)) {
                        continue;
                    }
                    if (axisCount[orient] > 0 && !explicit) {
                        // Change axis orient if the number do not match
                        const oppositeOrient = OPPOSITE_ORIENT[orient];
                        if (axisCount[orient] > axisCount[oppositeOrient]) {
                            axisComponent.set('orient', oppositeOrient, false);
                        }
                    }
                    axisCount[orient]++;
                    // TODO(https://github.com/vega/vega-lite/issues/2634): automatically add extra offset?
                }
            }
            // After merging, make sure to remove axes from child
            delete child.component.axes[channel];
        }
        // Suppress grid lines for dual axis charts (https://github.com/vega/vega-lite/issues/4676)
        if (resolve.axis[channel] === 'independent' && axes[channel] && axes[channel].length > 1) {
            for (const axisCmpt of axes[channel]) {
                if (!!axisCmpt.get('grid') && !axisCmpt.explicit.grid) {
                    axisCmpt.implicit.grid = false;
                }
            }
        }
    }
}
function mergeAxisComponents(mergedAxisCmpts, childAxisCmpts) {
    if (mergedAxisCmpts) {
        // FIXME: this is a bit wrong once we support multiple axes
        if (mergedAxisCmpts.length !== childAxisCmpts.length) {
            return undefined; // Cannot merge axis component with different number of axes.
        }
        const length = mergedAxisCmpts.length;
        for (let i = 0; i < length; i++) {
            const merged = mergedAxisCmpts[i];
            const child = childAxisCmpts[i];
            if (!!merged !== !!child) {
                return undefined;
            }
            else if (merged && child) {
                const mergedOrient = merged.getWithExplicit('orient');
                const childOrient = child.getWithExplicit('orient');
                if (mergedOrient.explicit && childOrient.explicit && mergedOrient.value !== childOrient.value) {
                    // TODO: throw warning if resolve is explicit (We don't have info about explicit/implicit resolve yet.)
                    // Cannot merge due to inconsistent orient
                    return undefined;
                }
                else {
                    mergedAxisCmpts[i] = mergeAxisComponent(merged, child);
                }
            }
        }
    }
    else {
        // For first one, return a copy of the child
        return childAxisCmpts.map(axisComponent => axisComponent.clone());
    }
    return mergedAxisCmpts;
}
function mergeAxisComponent(merged, child) {
    for (const prop of AXIS_COMPONENT_PROPERTIES) {
        const mergedValueWithExplicit = mergeValuesWithExplicit(merged.getWithExplicit(prop), child.getWithExplicit(prop), prop, 'axis', 
        // Tie breaker function
        (v1, v2) => {
            switch (prop) {
                case 'title':
                    return mergeTitleComponent(v1, v2);
                case 'gridScale':
                    return {
                        explicit: v1.explicit,
                        value: getFirstDefined(v1.value, v2.value)
                    };
            }
            return defaultTieBreaker(v1, v2, prop, 'axis');
        });
        merged.setWithExplicit(prop, mergedValueWithExplicit);
    }
    return merged;
}
function isExplicit(value, property, axis, model, channel) {
    if (property === 'disable') {
        return axis !== undefined; // if axis is specified or null/false, then its enable/disable state is explicit
    }
    axis = axis || {};
    switch (property) {
        case 'titleAngle':
        case 'labelAngle':
            return value === (isSignalRef(axis.labelAngle) ? axis.labelAngle : normalizeAngle(axis.labelAngle));
        case 'values':
            return !!axis.values;
        // specified axis.values is already respected, but may get transformed.
        case 'encode':
            // both VL axis.encoding and axis.labelAngle affect VG axis.encode
            return !!axis.encoding || !!axis.labelAngle;
        case 'title':
            // title can be explicit if fieldDef.title is set
            if (value === getFieldDefTitle(model, channel)) {
                return true;
            }
    }
    // Otherwise, things are explicit if the returned value matches the specified property
    return value === axis[property];
}
/**
 * Properties to always include values from config
 */
const propsToAlwaysIncludeConfig = new Set([
    'grid',
    'translate',
    // the rest are not axis configs in Vega, but are in VL, so we need to set too.
    'format',
    'formatType',
    'orient',
    'labelExpr',
    'tickCount',
    'position',
    'tickMinStep'
]);
function parseAxis(channel, model) {
    var _a, _b, _c;
    let axis = model.axis(channel);
    const axisComponent = new AxisComponent();
    const fieldOrDatumDef = getFieldOrDatumDef(model.encoding[channel]);
    const { mark, config } = model;
    const orient = (axis === null || axis === void 0 ? void 0 : axis.orient) ||
        ((_a = config[channel === 'x' ? 'axisX' : 'axisY']) === null || _a === void 0 ? void 0 : _a.orient) ||
        ((_b = config.axis) === null || _b === void 0 ? void 0 : _b.orient) ||
        defaultOrient(channel);
    const scaleType = model.getScaleComponent(channel).get('type');
    const axisConfigs = getAxisConfigs(channel, scaleType, orient, model.config);
    const disable = axis !== undefined ? !axis : getAxisConfig('disable', config.style, axis === null || axis === void 0 ? void 0 : axis.style, axisConfigs).configValue;
    axisComponent.set('disable', disable, axis !== undefined);
    if (disable) {
        return axisComponent;
    }
    axis = axis || {};
    const labelAngle = getLabelAngle(fieldOrDatumDef, axis, channel, config.style, axisConfigs);
    const ruleParams = {
        fieldOrDatumDef,
        axis,
        channel,
        model,
        scaleType,
        orient,
        labelAngle,
        mark,
        config
    };
    // 1.2. Add properties
    for (const property of AXIS_COMPONENT_PROPERTIES) {
        const value = property in axisRules ? axisRules[property](ruleParams) : isAxisProperty(property) ? axis[property] : undefined;
        const hasValue = value !== undefined;
        const explicit = isExplicit(value, property, axis, model, channel);
        if (hasValue && explicit) {
            axisComponent.set(property, value, explicit);
        }
        else {
            const { configValue = undefined, configFrom = undefined } = isAxisProperty(property) && property !== 'values'
                ? getAxisConfig(property, config.style, axis.style, axisConfigs)
                : {};
            const hasConfigValue = configValue !== undefined;
            if (hasValue && !hasConfigValue) {
                // only set property if it is explicitly set or has no config value (otherwise we will accidentally override config)
                axisComponent.set(property, value, explicit);
            }
            else if (
            // Cases need implicit values
            // 1. Axis config that aren't available in Vega
            !(configFrom === 'vgAxisConfig') ||
                // 2. Certain properties are always included (see `propsToAlwaysIncludeConfig`'s declaration for more details)
                (propsToAlwaysIncludeConfig.has(property) && hasConfigValue) ||
                // 3. Conditional axis values and signals
                isConditionalAxisValue(configValue) ||
                isSignalRef(configValue)) {
                // If a config is specified and is conditional, copy conditional value from axis config
                axisComponent.set(property, configValue, false);
            }
        }
    }
    // 2) Add guide encode definition groups
    const axisEncoding = (_c = axis.encoding) !== null && _c !== void 0 ? _c : {};
    const axisEncode = AXIS_PARTS.reduce((e, part) => {
        var _a;
        if (!axisComponent.hasAxisPart(part)) {
            // No need to create encode for a disabled part.
            return e;
        }
        const axisEncodingPart = guideEncodeEntry((_a = axisEncoding[part]) !== null && _a !== void 0 ? _a : {}, model);
        const value = part === 'labels' ? encode.labels(model, channel, axisEncodingPart) : axisEncodingPart;
        if (value !== undefined && !isEmpty(value)) {
            e[part] = { update: value };
        }
        return e;
    }, {});
    // FIXME: By having encode as one property, we won't have fine grained encode merging.
    if (!isEmpty(axisEncode)) {
        axisComponent.set('encode', axisEncode, !!axis.encoding || axis.labelAngle !== undefined);
    }
    return axisComponent;
}
//# sourceMappingURL=parse.js.map