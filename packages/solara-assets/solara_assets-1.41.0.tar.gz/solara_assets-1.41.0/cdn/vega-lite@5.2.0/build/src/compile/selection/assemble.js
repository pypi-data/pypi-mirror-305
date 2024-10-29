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
import { parseSelector } from 'vega-event-selector';
import { identity, isArray, stringValue } from 'vega-util';
import { MODIFY, STORE, unitName, VL_SELECTION_RESOLVE, TUPLE, selectionCompilers } from '.';
import { dateTimeToExpr, isDateTime, dateTimeToTimestamp } from '../../datetime';
import { hasContinuousDomain } from '../../scale';
import { keys, stringify, vals } from '../../util';
import { isUnitModel } from '../model';
import { parseSelectionExtent } from './parse';
export function assembleInit(init, isExpr = true, wrap = identity) {
    if (isArray(init)) {
        const assembled = init.map(v => assembleInit(v, isExpr, wrap));
        return isExpr ? `[${assembled.join(', ')}]` : assembled;
    }
    else if (isDateTime(init)) {
        if (isExpr) {
            return wrap(dateTimeToExpr(init));
        }
        else {
            return wrap(dateTimeToTimestamp(init));
        }
    }
    return isExpr ? wrap(stringify(init)) : init;
}
export function assembleUnitSelectionSignals(model, signals) {
    var _a;
    for (const selCmpt of vals((_a = model.component.selection) !== null && _a !== void 0 ? _a : {})) {
        const name = selCmpt.name;
        let modifyExpr = `${name}${TUPLE}, ${selCmpt.resolve === 'global' ? 'true' : `{unit: ${unitName(model)}}`}`;
        for (const c of selectionCompilers) {
            if (!c.defined(selCmpt))
                continue;
            if (c.signals)
                signals = c.signals(model, selCmpt, signals);
            if (c.modifyExpr)
                modifyExpr = c.modifyExpr(model, selCmpt, modifyExpr);
        }
        signals.push({
            name: name + MODIFY,
            on: [
                {
                    events: { signal: selCmpt.name + TUPLE },
                    update: `modify(${stringValue(selCmpt.name + STORE)}, ${modifyExpr})`
                }
            ]
        });
    }
    return cleanupEmptyOnArray(signals);
}
export function assembleFacetSignals(model, signals) {
    if (model.component.selection && keys(model.component.selection).length) {
        const name = stringValue(model.getName('cell'));
        signals.unshift({
            name: 'facet',
            value: {},
            on: [
                {
                    events: parseSelector('mousemove', 'scope'),
                    update: `isTuple(facet) ? facet : group(${name}).datum`
                }
            ]
        });
    }
    return cleanupEmptyOnArray(signals);
}
export function assembleTopLevelSignals(model, signals) {
    var _a;
    let hasSelections = false;
    for (const selCmpt of vals((_a = model.component.selection) !== null && _a !== void 0 ? _a : {})) {
        const name = selCmpt.name;
        const store = stringValue(name + STORE);
        const hasSg = signals.filter(s => s.name === name);
        if (hasSg.length === 0) {
            const resolve = selCmpt.resolve === 'global' ? 'union' : selCmpt.resolve;
            const isPoint = selCmpt.type === 'point' ? ', true, true)' : ')';
            signals.push({
                name: selCmpt.name,
                update: `${VL_SELECTION_RESOLVE}(${store}, ${stringValue(resolve)}${isPoint}`
            });
        }
        hasSelections = true;
        for (const c of selectionCompilers) {
            if (c.defined(selCmpt) && c.topLevelSignals) {
                signals = c.topLevelSignals(model, selCmpt, signals);
            }
        }
    }
    if (hasSelections) {
        const hasUnit = signals.filter(s => s.name === 'unit');
        if (hasUnit.length === 0) {
            signals.unshift({
                name: 'unit',
                value: {},
                on: [{ events: 'mousemove', update: 'isTuple(group()) ? group() : unit' }]
            });
        }
    }
    return cleanupEmptyOnArray(signals);
}
export function assembleUnitSelectionData(model, data) {
    var _a;
    const dataCopy = [...data];
    for (const selCmpt of vals((_a = model.component.selection) !== null && _a !== void 0 ? _a : {})) {
        const init = { name: selCmpt.name + STORE };
        if (selCmpt.init) {
            const fields = selCmpt.project.items.map(proj => {
                const { signals } = proj, rest = __rest(proj, ["signals"]);
                return rest;
            });
            init.values = selCmpt.init.map(i => ({
                unit: unitName(model, { escape: false }),
                fields,
                values: assembleInit(i, false)
            }));
        }
        const contains = dataCopy.filter(d => d.name === selCmpt.name + STORE);
        if (!contains.length) {
            dataCopy.push(init);
        }
    }
    return dataCopy;
}
export function assembleUnitSelectionMarks(model, marks) {
    var _a;
    for (const selCmpt of vals((_a = model.component.selection) !== null && _a !== void 0 ? _a : {})) {
        for (const c of selectionCompilers) {
            if (c.defined(selCmpt) && c.marks) {
                marks = c.marks(model, selCmpt, marks);
            }
        }
    }
    return marks;
}
export function assembleLayerSelectionMarks(model, marks) {
    for (const child of model.children) {
        if (isUnitModel(child)) {
            marks = assembleUnitSelectionMarks(child, marks);
        }
    }
    return marks;
}
export function assembleSelectionScaleDomain(model, extent, scaleCmpt, domain) {
    const parsedExtent = parseSelectionExtent(model, extent.param, extent);
    return {
        signal: hasContinuousDomain(scaleCmpt.get('type')) && isArray(domain) && domain[0] > domain[1]
            ? `isValid(${parsedExtent}) && reverse(${parsedExtent})`
            : parsedExtent
    };
}
function cleanupEmptyOnArray(signals) {
    return signals.map(s => {
        if (s.on && !s.on.length)
            delete s.on;
        return s;
    });
}
//# sourceMappingURL=assemble.js.map