import { stringValue } from 'vega-util';
import { VL_SELECTION_RESOLVE } from '.';
import { isScaleChannel } from '../../channel';
import * as log from '../../log';
import { hasContinuousDomain } from '../../scale';
import { isLayerModel } from '../model';
import { replacePathInField } from '../../util';
const scaleBindings = {
    defined: selCmpt => {
        return selCmpt.type === 'interval' && selCmpt.resolve === 'global' && selCmpt.bind && selCmpt.bind === 'scales';
    },
    parse: (model, selCmpt) => {
        const bound = (selCmpt.scales = []);
        for (const proj of selCmpt.project.items) {
            const channel = proj.channel;
            if (!isScaleChannel(channel)) {
                continue;
            }
            const scale = model.getScaleComponent(channel);
            const scaleType = scale ? scale.get('type') : undefined;
            if (!scale || !hasContinuousDomain(scaleType)) {
                log.warn(log.message.SCALE_BINDINGS_CONTINUOUS);
                continue;
            }
            scale.set('selectionExtent', { param: selCmpt.name, field: proj.field }, true);
            bound.push(proj);
        }
    },
    topLevelSignals: (model, selCmpt, signals) => {
        const bound = selCmpt.scales.filter(proj => signals.filter(s => s.name === proj.signals.data).length === 0);
        // Top-level signals are only needed for multiview displays and if this
        // view's top-level signals haven't already been generated.
        if (!model.parent || isTopLevelLayer(model) || bound.length === 0) {
            return signals;
        }
        // vlSelectionResolve does not account for the behavior of bound scales in
        // multiview displays. Each unit view adds a tuple to the store, but the
        // state of the selection is the unit selection most recently updated. This
        // state is captured by the top-level signals that we insert and "push
        // outer" to from within the units. We need to reassemble this state into
        // the top-level named signal, except no single selCmpt has a global view.
        const namedSg = signals.filter(s => s.name === selCmpt.name)[0];
        let update = namedSg.update;
        if (update.indexOf(VL_SELECTION_RESOLVE) >= 0) {
            namedSg.update = `{${bound
                .map(proj => `${stringValue(replacePathInField(proj.field))}: ${proj.signals.data}`)
                .join(', ')}}`;
        }
        else {
            for (const proj of bound) {
                const mapping = `${stringValue(replacePathInField(proj.field))}: ${proj.signals.data}`;
                if (!update.includes(mapping)) {
                    update = `${update.substring(0, update.length - 1)}, ${mapping}}`;
                }
            }
            namedSg.update = update;
        }
        return signals.concat(bound.map(proj => ({ name: proj.signals.data })));
    },
    signals: (model, selCmpt, signals) => {
        // Nested signals need only push to top-level signals with multiview displays.
        if (model.parent && !isTopLevelLayer(model)) {
            for (const proj of selCmpt.scales) {
                const signal = signals.filter(s => s.name === proj.signals.data)[0];
                signal.push = 'outer';
                delete signal.value;
                delete signal.update;
            }
        }
        return signals;
    }
};
export default scaleBindings;
export function domain(model, channel) {
    const scale = stringValue(model.scaleName(channel));
    return `domain(${scale})`;
}
function isTopLevelLayer(model) {
    var _a;
    return model.parent && isLayerModel(model.parent) && ((_a = !model.parent.parent) !== null && _a !== void 0 ? _a : isTopLevelLayer(model.parent.parent));
}
//# sourceMappingURL=scales.js.map