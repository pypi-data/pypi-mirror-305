import { isArgmaxDef, isArgminDef } from '../../aggregate';
import { getPositionChannelFromLatLong, getSecondaryRangeChannel, isGeoPositionChannel, isScaleChannel } from '../../channel';
import { binRequiresRange, hasBandEnd, isScaleFieldDef, isTypedFieldDef, vgField } from '../../channeldef';
import * as log from '../../log';
import { isFieldRange } from '../../scale';
import { duplicate, hash, keys, replacePathInField, setEqual } from '../../util';
import { isUnitModel } from '../model';
import { DataFlowNode } from './dataflow';
function addDimension(dims, channel, fieldDef, model) {
    var _a;
    const channelDef2 = isUnitModel(model) ? model.encoding[getSecondaryRangeChannel(channel)] : undefined;
    if (isTypedFieldDef(fieldDef) &&
        isUnitModel(model) &&
        hasBandEnd(fieldDef, channelDef2, model.markDef, model.config)) {
        dims.add(vgField(fieldDef, {}));
        dims.add(vgField(fieldDef, { suffix: 'end' }));
        if (fieldDef.bin && binRequiresRange(fieldDef, channel)) {
            dims.add(vgField(fieldDef, { binSuffix: 'range' }));
        }
    }
    else if (isGeoPositionChannel(channel)) {
        const posChannel = getPositionChannelFromLatLong(channel);
        dims.add(model.getName(posChannel));
    }
    else {
        dims.add(vgField(fieldDef));
    }
    if (isScaleFieldDef(fieldDef) && isFieldRange((_a = fieldDef.scale) === null || _a === void 0 ? void 0 : _a.range)) {
        dims.add(fieldDef.scale.range.field);
    }
    return dims;
}
function mergeMeasures(parentMeasures, childMeasures) {
    var _a;
    for (const field of keys(childMeasures)) {
        // when we merge a measure, we either have to add an aggregation operator or even a new field
        const ops = childMeasures[field];
        for (const op of keys(ops)) {
            if (field in parentMeasures) {
                // add operator to existing measure field
                parentMeasures[field][op] = new Set([...((_a = parentMeasures[field][op]) !== null && _a !== void 0 ? _a : []), ...ops[op]]);
            }
            else {
                parentMeasures[field] = { [op]: ops[op] };
            }
        }
    }
}
export class AggregateNode extends DataFlowNode {
    /**
     * @param dimensions string set for dimensions
     * @param measures dictionary mapping field name => dict of aggregation functions and names to use
     */
    constructor(parent, dimensions, measures) {
        super(parent);
        this.dimensions = dimensions;
        this.measures = measures;
    }
    clone() {
        return new AggregateNode(null, new Set(this.dimensions), duplicate(this.measures));
    }
    get groupBy() {
        return this.dimensions;
    }
    static makeFromEncoding(parent, model) {
        let isAggregate = false;
        model.forEachFieldDef(fd => {
            if (fd.aggregate) {
                isAggregate = true;
            }
        });
        const meas = {};
        const dims = new Set();
        if (!isAggregate) {
            // no need to create this node if the model has no aggregation
            return null;
        }
        model.forEachFieldDef((fieldDef, channel) => {
            var _a, _b, _c, _d;
            const { aggregate, field } = fieldDef;
            if (aggregate) {
                if (aggregate === 'count') {
                    (_a = meas['*']) !== null && _a !== void 0 ? _a : (meas['*'] = {});
                    meas['*']['count'] = new Set([vgField(fieldDef, { forAs: true })]);
                }
                else {
                    if (isArgminDef(aggregate) || isArgmaxDef(aggregate)) {
                        const op = isArgminDef(aggregate) ? 'argmin' : 'argmax';
                        const argField = aggregate[op];
                        (_b = meas[argField]) !== null && _b !== void 0 ? _b : (meas[argField] = {});
                        meas[argField][op] = new Set([vgField({ op, field: argField }, { forAs: true })]);
                    }
                    else {
                        (_c = meas[field]) !== null && _c !== void 0 ? _c : (meas[field] = {});
                        meas[field][aggregate] = new Set([vgField(fieldDef, { forAs: true })]);
                    }
                    // For scale channel with domain === 'unaggregated', add min/max so we can use their union as unaggregated domain
                    if (isScaleChannel(channel) && model.scaleDomain(channel) === 'unaggregated') {
                        (_d = meas[field]) !== null && _d !== void 0 ? _d : (meas[field] = {});
                        meas[field]['min'] = new Set([vgField({ field, aggregate: 'min' }, { forAs: true })]);
                        meas[field]['max'] = new Set([vgField({ field, aggregate: 'max' }, { forAs: true })]);
                    }
                }
            }
            else {
                addDimension(dims, channel, fieldDef, model);
            }
        });
        if (dims.size + keys(meas).length === 0) {
            return null;
        }
        return new AggregateNode(parent, dims, meas);
    }
    static makeFromTransform(parent, t) {
        var _a, _b, _c;
        const dims = new Set();
        const meas = {};
        for (const s of t.aggregate) {
            const { op, field, as } = s;
            if (op) {
                if (op === 'count') {
                    (_a = meas['*']) !== null && _a !== void 0 ? _a : (meas['*'] = {});
                    meas['*']['count'] = new Set([as ? as : vgField(s, { forAs: true })]);
                }
                else {
                    (_b = meas[field]) !== null && _b !== void 0 ? _b : (meas[field] = {});
                    meas[field][op] = new Set([as ? as : vgField(s, { forAs: true })]);
                }
            }
        }
        for (const s of (_c = t.groupby) !== null && _c !== void 0 ? _c : []) {
            dims.add(s);
        }
        if (dims.size + keys(meas).length === 0) {
            return null;
        }
        return new AggregateNode(parent, dims, meas);
    }
    merge(other) {
        if (setEqual(this.dimensions, other.dimensions)) {
            mergeMeasures(this.measures, other.measures);
            return true;
        }
        log.debug('different dimensions, cannot merge');
        return false;
    }
    addDimensions(fields) {
        fields.forEach(this.dimensions.add, this.dimensions);
    }
    dependentFields() {
        return new Set([...this.dimensions, ...keys(this.measures)]);
    }
    producedFields() {
        const out = new Set();
        for (const field of keys(this.measures)) {
            for (const op of keys(this.measures[field])) {
                const m = this.measures[field][op];
                if (m.size === 0) {
                    out.add(`${op}_${field}`);
                }
                else {
                    m.forEach(out.add, out);
                }
            }
        }
        return out;
    }
    hash() {
        return `Aggregate ${hash({ dimensions: this.dimensions, measures: this.measures })}`;
    }
    assemble() {
        const ops = [];
        const fields = [];
        const as = [];
        for (const field of keys(this.measures)) {
            for (const op of keys(this.measures[field])) {
                for (const alias of this.measures[field][op]) {
                    as.push(alias);
                    ops.push(op);
                    fields.push(field === '*' ? null : replacePathInField(field));
                }
            }
        }
        const result = {
            type: 'aggregate',
            groupby: [...this.dimensions].map(replacePathInField),
            ops,
            fields,
            as
        };
        return result;
    }
}
//# sourceMappingURL=aggregate.js.map