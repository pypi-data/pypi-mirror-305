import { stringValue } from 'vega-util';
import { disableDirectManipulation, TUPLE } from '.';
import { varName } from '../../util';
import { assembleInit } from './assemble';
import nearest from './nearest';
import { TUPLE_FIELDS } from './project';
import { isLegendBinding } from '../../selection';
const inputBindings = {
    defined: selCmpt => {
        return (selCmpt.type === 'point' &&
            selCmpt.resolve === 'global' &&
            selCmpt.bind &&
            selCmpt.bind !== 'scales' &&
            !isLegendBinding(selCmpt.bind));
    },
    parse: (model, selCmpt, selDef) => disableDirectManipulation(selCmpt, selDef),
    topLevelSignals: (model, selCmpt, signals) => {
        const name = selCmpt.name;
        const proj = selCmpt.project;
        const bind = selCmpt.bind;
        const init = selCmpt.init && selCmpt.init[0]; // Can only exist on single selections (one initial value).
        const datum = nearest.defined(selCmpt) ? '(item().isVoronoi ? datum.datum : datum)' : 'datum';
        proj.items.forEach((p, i) => {
            var _a, _b;
            const sgname = varName(`${name}_${p.field}`);
            const hasSignal = signals.filter(s => s.name === sgname);
            if (!hasSignal.length) {
                signals.unshift(Object.assign(Object.assign({ name: sgname }, (init ? { init: assembleInit(init[i]) } : { value: null })), { on: selCmpt.events
                        ? [
                            {
                                events: selCmpt.events,
                                update: `datum && item().mark.marktype !== 'group' ? ${datum}[${stringValue(p.field)}] : null`
                            }
                        ]
                        : [], bind: (_b = (_a = bind[p.field]) !== null && _a !== void 0 ? _a : bind[p.channel]) !== null && _b !== void 0 ? _b : bind }));
            }
        });
        return signals;
    },
    signals: (model, selCmpt, signals) => {
        const name = selCmpt.name;
        const proj = selCmpt.project;
        const signal = signals.filter(s => s.name === name + TUPLE)[0];
        const fields = name + TUPLE_FIELDS;
        const values = proj.items.map(p => varName(`${name}_${p.field}`));
        const valid = values.map(v => `${v} !== null`).join(' && ');
        if (values.length) {
            signal.update = `${valid} ? {fields: ${fields}, values: [${values.join(', ')}]} : null`;
        }
        delete signal.value;
        delete signal.on;
        return signals;
    }
};
export default inputBindings;
//# sourceMappingURL=inputs.js.map