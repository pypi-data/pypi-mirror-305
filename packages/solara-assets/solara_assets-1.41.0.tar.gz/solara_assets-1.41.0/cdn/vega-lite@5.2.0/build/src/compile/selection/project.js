var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
import { array, isObject } from 'vega-util';
import { isSingleDefUnitChannel } from '../../channel';
import * as log from '../../log';
import { hasContinuousDomain } from '../../scale';
import { hash, keys, replacePathInField, varName, isEmpty } from '../../util';
import { TimeUnitNode } from '../data/timeunit';
export const TUPLE_FIELDS = '_tuple_fields';
export class SelectionProjectionComponent {
    constructor(...items) {
        this.items = items;
        this.hasChannel = {};
        this.hasField = {};
    }
}
const project = {
    defined: () => {
        return true; // This transform handles its own defaults, so always run parse.
    },
    parse: (model, selCmpt, selDef) => {
        var _a;
        const name = selCmpt.name;
        const proj = ((_a = selCmpt.project) !== null && _a !== void 0 ? _a : (selCmpt.project = new SelectionProjectionComponent()));
        const parsed = {};
        const timeUnits = {};
        const signals = new Set();
        const signalName = (p, range) => {
            const suffix = range === 'visual' ? p.channel : p.field;
            let sg = varName(`${name}_${suffix}`);
            for (let counter = 1; signals.has(sg); counter++) {
                sg = varName(`${name}_${suffix}_${counter}`);
            }
            signals.add(sg);
            return { [range]: sg };
        };
        const type = selCmpt.type;
        const cfg = model.config.selection[type];
        const init = selDef.value !== undefined
            ? array(selDef.value)
            : null;
        // If no explicit projection (either fields or encodings) is specified, set some defaults.
        // If an initial value is set, try to infer projections.
        let { fields, encodings } = (isObject(selDef.select) ? selDef.select : {});
        if (!fields && !encodings && init) {
            for (const initVal of init) {
                // initVal may be a scalar value to smoothen varParam -> pointSelection gradient.
                if (!isObject(initVal)) {
                    continue;
                }
                for (const key of keys(initVal)) {
                    if (isSingleDefUnitChannel(key)) {
                        (encodings || (encodings = [])).push(key);
                    }
                    else {
                        if (type === 'interval') {
                            log.warn(log.message.INTERVAL_INITIALIZED_WITH_X_Y);
                            encodings = cfg.encodings;
                        }
                        else {
                            (fields || (fields = [])).push(key);
                        }
                    }
                }
            }
        }
        // If no initial value is specified, use the default configuration.
        // We break this out as a separate if block (instead of an else condition)
        // to account for unprojected point selections that have scalar initial values
        if (!fields && !encodings) {
            encodings = cfg.encodings;
            if ('fields' in cfg) {
                fields = cfg.fields;
            }
        }
        for (const channel of encodings !== null && encodings !== void 0 ? encodings : []) {
            const fieldDef = model.fieldDef(channel);
            if (fieldDef) {
                let field = fieldDef.field;
                if (fieldDef.aggregate) {
                    log.warn(log.message.cannotProjectAggregate(channel, fieldDef.aggregate));
                    continue;
                }
                else if (!field) {
                    log.warn(log.message.cannotProjectOnChannelWithoutField(channel));
                    continue;
                }
                if (fieldDef.timeUnit) {
                    field = model.vgField(channel);
                    // Construct TimeUnitComponents which will be combined into a
                    // TimeUnitNode. This node may need to be inserted into the
                    // dataflow if the selection is used across views that do not
                    // have these time units defined.
                    const component = {
                        timeUnit: fieldDef.timeUnit,
                        as: field,
                        field: fieldDef.field
                    };
                    timeUnits[hash(component)] = component;
                }
                // Prevent duplicate projections on the same field.
                // TODO: what if the same field is bound to multiple channels (e.g., SPLOM diag).
                if (!parsed[field]) {
                    // Determine whether the tuple will store enumerated or ranged values.
                    // Interval selections store ranges for continuous scales, and enumerations otherwise.
                    // Single/multi selections store ranges for binned fields, and enumerations otherwise.
                    let tplType = 'E';
                    if (type === 'interval') {
                        const scaleType = model.getScaleComponent(channel).get('type');
                        if (hasContinuousDomain(scaleType)) {
                            tplType = 'R';
                        }
                    }
                    else if (fieldDef.bin) {
                        tplType = 'R-RE';
                    }
                    const p = { field, channel, type: tplType };
                    p.signals = Object.assign(Object.assign({}, signalName(p, 'data')), signalName(p, 'visual'));
                    proj.items.push((parsed[field] = p));
                    proj.hasField[field] = proj.hasChannel[channel] = parsed[field];
                }
            }
            else {
                log.warn(log.message.cannotProjectOnChannelWithoutField(channel));
            }
        }
        for (const field of fields !== null && fields !== void 0 ? fields : []) {
            if (proj.hasField[field])
                continue;
            const p = { type: 'E', field };
            p.signals = Object.assign({}, signalName(p, 'data'));
            proj.items.push(p);
            proj.hasField[field] = p;
        }
        if (init) {
            selCmpt.init = init.map((v) => {
                // Selections can be initialized either with a full object that maps projections to values
                // or scalar values to smoothen the abstraction gradient from variable params to point selections.
                return proj.items.map(p => (isObject(v) ? (v[p.channel] !== undefined ? v[p.channel] : v[p.field]) : v));
            });
        }
        if (!isEmpty(timeUnits)) {
            proj.timeUnit = new TimeUnitNode(null, timeUnits);
        }
    },
    signals: (model, selCmpt, allSignals) => {
        const name = selCmpt.name + TUPLE_FIELDS;
        const hasSignal = allSignals.filter(s => s.name === name);
        return hasSignal.length > 0
            ? allSignals
            : allSignals.concat({
                name,
                value: selCmpt.project.items.map(proj => {
                    const { signals, hasLegend } = proj, rest = __rest(proj, ["signals", "hasLegend"]);
                    rest.field = replacePathInField(rest.field);
                    return rest;
                })
            });
    }
};
export default project;
//# sourceMappingURL=project.js.map