import { isNumber } from 'vega-util';
import { getViewConfigDiscreteStep } from '../../config';
import { isVgRangeStep } from '../../vega.schema';
import { getMarkPropOrConfig, signalOrValueRef } from '../common';
import * as encode from './encode';
export const tick = {
    vgMark: 'rect',
    encodeEntry: (model) => {
        const { config, markDef } = model;
        const orient = markDef.orient;
        const vgSizeChannel = orient === 'horizontal' ? 'width' : 'height';
        const vgThicknessChannel = orient === 'horizontal' ? 'height' : 'width';
        return Object.assign(Object.assign(Object.assign(Object.assign(Object.assign({}, encode.baseEncodeEntry(model, {
            align: 'ignore',
            baseline: 'ignore',
            color: 'include',
            orient: 'ignore',
            size: 'ignore',
            theta: 'ignore'
        })), encode.pointPosition('x', model, { defaultPos: 'mid', vgChannel: 'xc' })), encode.pointPosition('y', model, { defaultPos: 'mid', vgChannel: 'yc' })), encode.nonPosition('size', model, {
            defaultValue: defaultSize(model),
            vgChannel: vgSizeChannel
        })), { [vgThicknessChannel]: signalOrValueRef(getMarkPropOrConfig('thickness', markDef, config)) });
    }
};
function defaultSize(model) {
    var _a;
    const { config, markDef } = model;
    const { orient } = markDef;
    const vgSizeChannel = orient === 'horizontal' ? 'width' : 'height';
    const scale = model.getScaleComponent(orient === 'horizontal' ? 'x' : 'y');
    const markPropOrConfig = (_a = getMarkPropOrConfig('size', markDef, config, { vgChannel: vgSizeChannel })) !== null && _a !== void 0 ? _a : config.tick.bandSize;
    if (markPropOrConfig !== undefined) {
        return markPropOrConfig;
    }
    else {
        const scaleRange = scale ? scale.get('range') : undefined;
        if (scaleRange && isVgRangeStep(scaleRange) && isNumber(scaleRange.step)) {
            return (scaleRange.step * 3) / 4;
        }
        const defaultViewStep = getViewConfigDiscreteStep(config.view, vgSizeChannel);
        return (defaultViewStep * 3) / 4;
    }
}
//# sourceMappingURL=tick.js.map