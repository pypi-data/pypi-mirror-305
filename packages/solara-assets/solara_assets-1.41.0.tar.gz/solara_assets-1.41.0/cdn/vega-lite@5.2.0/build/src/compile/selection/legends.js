import { isObject } from 'vega';
import { parseSelector } from 'vega-event-selector';
import { array, isString } from 'vega-util';
import { disableDirectManipulation, TUPLE } from '.';
import * as log from '../../log';
import { isLegendBinding, isLegendStreamBinding, SELECTION_ID } from '../../selection';
import { duplicate, vals, varName } from '../../util';
import { TUPLE_FIELDS } from './project';
import { TOGGLE } from './toggle';
const legendBindings = {
    defined: selCmpt => {
        const spec = selCmpt.resolve === 'global' && selCmpt.bind && isLegendBinding(selCmpt.bind);
        const projLen = selCmpt.project.items.length === 1 && selCmpt.project.items[0].field !== SELECTION_ID;
        if (spec && !projLen) {
            log.warn(log.message.LEGEND_BINDINGS_MUST_HAVE_PROJECTION);
        }
        return spec && projLen;
    },
    parse: (model, selCmpt, selDef) => {
        var _a;
        // Allow legend items to be toggleable by default even though direct manipulation is disabled.
        const selDef_ = duplicate(selDef);
        selDef_.select = isString(selDef_.select)
            ? { type: selDef_.select, toggle: selCmpt.toggle }
            : Object.assign(Object.assign({}, selDef_.select), { toggle: selCmpt.toggle });
        disableDirectManipulation(selCmpt, selDef_);
        if (isObject(selDef.select) && (selDef.select.on || selDef.select.clear)) {
            const legendFilter = 'event.item && indexof(event.item.mark.role, "legend") < 0';
            for (const evt of selCmpt.events) {
                evt.filter = array((_a = evt.filter) !== null && _a !== void 0 ? _a : []);
                if (!evt.filter.includes(legendFilter)) {
                    evt.filter.push(legendFilter);
                }
            }
        }
        const evt = isLegendStreamBinding(selCmpt.bind) ? selCmpt.bind.legend : 'click';
        const stream = isString(evt) ? parseSelector(evt, 'view') : array(evt);
        selCmpt.bind = { legend: { merge: stream } };
    },
    topLevelSignals: (model, selCmpt, signals) => {
        const selName = selCmpt.name;
        const stream = isLegendStreamBinding(selCmpt.bind) && selCmpt.bind.legend;
        const markName = (name) => (s) => {
            const ds = duplicate(s);
            ds.markname = name;
            return ds;
        };
        for (const proj of selCmpt.project.items) {
            if (!proj.hasLegend)
                continue;
            const prefix = `${varName(proj.field)}_legend`;
            const sgName = `${selName}_${prefix}`;
            const hasSignal = signals.filter(s => s.name === sgName);
            if (hasSignal.length === 0) {
                const events = stream.merge
                    .map(markName(`${prefix}_symbols`))
                    .concat(stream.merge.map(markName(`${prefix}_labels`)))
                    .concat(stream.merge.map(markName(`${prefix}_entries`)));
                signals.unshift(Object.assign(Object.assign({ name: sgName }, (!selCmpt.init ? { value: null } : {})), { on: [
                        // Legend entries do not store values, so we need to walk the scenegraph to the symbol datum.
                        { events, update: 'datum.value || item().items[0].items[0].datum.value', force: true },
                        { events: stream.merge, update: `!event.item || !datum ? null : ${sgName}`, force: true }
                    ] }));
            }
        }
        return signals;
    },
    signals: (model, selCmpt, signals) => {
        const name = selCmpt.name;
        const proj = selCmpt.project;
        const tuple = signals.find(s => s.name === name + TUPLE);
        const fields = name + TUPLE_FIELDS;
        const values = proj.items.filter(p => p.hasLegend).map(p => varName(`${name}_${varName(p.field)}_legend`));
        const valid = values.map(v => `${v} !== null`).join(' && ');
        const update = `${valid} ? {fields: ${fields}, values: [${values.join(', ')}]} : null`;
        if (selCmpt.events && values.length > 0) {
            tuple.on.push({
                events: values.map(signal => ({ signal })),
                update
            });
        }
        else if (values.length > 0) {
            tuple.update = update;
            delete tuple.value;
            delete tuple.on;
        }
        const toggle = signals.find(s => s.name === name + TOGGLE);
        const events = isLegendStreamBinding(selCmpt.bind) && selCmpt.bind.legend;
        if (toggle) {
            if (!selCmpt.events)
                toggle.on[0].events = events;
            else
                toggle.on.push(Object.assign(Object.assign({}, toggle.on[0]), { events }));
        }
        return signals;
    }
};
export default legendBindings;
export function parseInteractiveLegend(model, channel, legendCmpt) {
    var _a, _b, _c, _d;
    const field = (_a = model.fieldDef(channel)) === null || _a === void 0 ? void 0 : _a.field;
    for (const selCmpt of vals((_b = model.component.selection) !== null && _b !== void 0 ? _b : {})) {
        const proj = (_c = selCmpt.project.hasField[field]) !== null && _c !== void 0 ? _c : selCmpt.project.hasChannel[channel];
        if (proj && legendBindings.defined(selCmpt)) {
            const legendSelections = (_d = legendCmpt.get('selections')) !== null && _d !== void 0 ? _d : [];
            legendSelections.push(selCmpt.name);
            legendCmpt.set('selections', legendSelections, false);
            proj.hasLegend = true;
        }
    }
}
//# sourceMappingURL=legends.js.map