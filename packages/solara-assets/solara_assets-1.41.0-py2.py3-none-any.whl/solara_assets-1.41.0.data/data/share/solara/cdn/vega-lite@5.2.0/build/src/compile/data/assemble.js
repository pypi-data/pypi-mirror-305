import { isUrlData } from '../../data';
import { AggregateNode } from './aggregate';
import { BinNode } from './bin';
import { CalculateNode } from './calculate';
import { OutputNode } from './dataflow';
import { DensityTransformNode } from './density';
import { FacetNode } from './facet';
import { FilterNode } from './filter';
import { FilterInvalidNode } from './filterinvalid';
import { FlattenTransformNode } from './flatten';
import { FoldTransformNode } from './fold';
import { ParseNode } from './formatparse';
import { GeoJSONNode } from './geojson';
import { GeoPointNode } from './geopoint';
import { GraticuleNode } from './graticule';
import { IdentifierNode } from './identifier';
import { ImputeNode } from './impute';
import { JoinAggregateTransformNode } from './joinaggregate';
import { LoessTransformNode } from './loess';
import { LookupNode } from './lookup';
import { QuantileTransformNode } from './quantile';
import { RegressionTransformNode } from './regression';
import { PivotTransformNode } from './pivot';
import { SampleTransformNode } from './sample';
import { SequenceNode } from './sequence';
import { SourceNode } from './source';
import { StackNode } from './stack';
import { TimeUnitNode } from './timeunit';
import { WindowTransformNode } from './window';
function makeWalkTree(data) {
    // to name datasources
    let datasetIndex = 0;
    /**
     * Recursively walk down the tree.
     */
    function walkTree(node, dataSource) {
        var _a;
        if (node instanceof SourceNode) {
            // If the source is a named data source or a data source with values, we need
            // to put it in a different data source. Otherwise, Vega may override the data.
            if (!node.isGenerator && !isUrlData(node.data)) {
                data.push(dataSource);
                const newData = {
                    name: null,
                    source: dataSource.name,
                    transform: []
                };
                dataSource = newData;
            }
        }
        if (node instanceof ParseNode) {
            if (node.parent instanceof SourceNode && !dataSource.source) {
                // If node's parent is a root source and the data source does not refer to another data source, use normal format parse
                dataSource.format = Object.assign(Object.assign({}, ((_a = dataSource.format) !== null && _a !== void 0 ? _a : {})), { parse: node.assembleFormatParse() });
                // add calculates for all nested fields
                dataSource.transform.push(...node.assembleTransforms(true));
            }
            else {
                // Otherwise use Vega expression to parse
                dataSource.transform.push(...node.assembleTransforms());
            }
        }
        if (node instanceof FacetNode) {
            if (!dataSource.name) {
                dataSource.name = `data_${datasetIndex++}`;
            }
            if (!dataSource.source || dataSource.transform.length > 0) {
                data.push(dataSource);
                node.data = dataSource.name;
            }
            else {
                node.data = dataSource.source;
            }
            data.push(...node.assemble());
            // break here because the rest of the tree has to be taken care of by the facet.
            return;
        }
        if (node instanceof GraticuleNode ||
            node instanceof SequenceNode ||
            node instanceof FilterInvalidNode ||
            node instanceof FilterNode ||
            node instanceof CalculateNode ||
            node instanceof GeoPointNode ||
            node instanceof AggregateNode ||
            node instanceof LookupNode ||
            node instanceof WindowTransformNode ||
            node instanceof JoinAggregateTransformNode ||
            node instanceof FoldTransformNode ||
            node instanceof FlattenTransformNode ||
            node instanceof DensityTransformNode ||
            node instanceof LoessTransformNode ||
            node instanceof QuantileTransformNode ||
            node instanceof RegressionTransformNode ||
            node instanceof IdentifierNode ||
            node instanceof SampleTransformNode ||
            node instanceof PivotTransformNode) {
            dataSource.transform.push(node.assemble());
        }
        if (node instanceof BinNode ||
            node instanceof TimeUnitNode ||
            node instanceof ImputeNode ||
            node instanceof StackNode ||
            node instanceof GeoJSONNode) {
            dataSource.transform.push(...node.assemble());
        }
        if (node instanceof OutputNode) {
            if (dataSource.source && dataSource.transform.length === 0) {
                node.setSource(dataSource.source);
            }
            else if (node.parent instanceof OutputNode) {
                // Note that an output node may be required but we still do not assemble a
                // separate data source for it.
                node.setSource(dataSource.name);
            }
            else {
                if (!dataSource.name) {
                    dataSource.name = `data_${datasetIndex++}`;
                }
                // Here we set the name of the datasource we generated. From now on
                // other assemblers can use it.
                node.setSource(dataSource.name);
                // if this node has more than one child, we will add a datasource automatically
                if (node.numChildren() === 1) {
                    data.push(dataSource);
                    const newData = {
                        name: null,
                        source: dataSource.name,
                        transform: []
                    };
                    dataSource = newData;
                }
            }
        }
        switch (node.numChildren()) {
            case 0:
                // done
                if (node instanceof OutputNode && (!dataSource.source || dataSource.transform.length > 0)) {
                    // do not push empty datasources that are simply references
                    data.push(dataSource);
                }
                break;
            case 1:
                walkTree(node.children[0], dataSource);
                break;
            default: {
                if (!dataSource.name) {
                    dataSource.name = `data_${datasetIndex++}`;
                }
                let source = dataSource.name;
                if (!dataSource.source || dataSource.transform.length > 0) {
                    data.push(dataSource);
                }
                else {
                    source = dataSource.source;
                }
                for (const child of node.children) {
                    const newData = {
                        name: null,
                        source,
                        transform: []
                    };
                    walkTree(child, newData);
                }
                break;
            }
        }
    }
    return walkTree;
}
/**
 * Assemble data sources that are derived from faceted data.
 */
export function assembleFacetData(root) {
    const data = [];
    const walkTree = makeWalkTree(data);
    for (const child of root.children) {
        walkTree(child, {
            source: root.name,
            name: null,
            transform: []
        });
    }
    return data;
}
/**
 * Create Vega data array from a given compiled model and append all of them to the given array
 *
 * @param  model
 * @param  data array
 * @return modified data array
 */
export function assembleRootData(dataComponent, datasets) {
    var _a, _b;
    const data = [];
    // dataComponent.sources.forEach(debug);
    // draw(dataComponent.sources);
    const walkTree = makeWalkTree(data);
    let sourceIndex = 0;
    for (const root of dataComponent.sources) {
        // assign a name if the source does not have a name yet
        if (!root.hasName()) {
            root.dataName = `source_${sourceIndex++}`;
        }
        const newData = root.assemble();
        walkTree(root, newData);
    }
    // remove empty transform arrays for cleaner output
    for (const d of data) {
        if (d.transform.length === 0) {
            delete d.transform;
        }
    }
    // move sources without transforms (the ones that are potentially used in lookups) to the beginning
    let whereTo = 0;
    for (const [i, d] of data.entries()) {
        if (((_a = d.transform) !== null && _a !== void 0 ? _a : []).length === 0 && !d.source) {
            data.splice(whereTo++, 0, data.splice(i, 1)[0]);
        }
    }
    // now fix the from references in lookup transforms
    for (const d of data) {
        for (const t of (_b = d.transform) !== null && _b !== void 0 ? _b : []) {
            if (t.type === 'lookup') {
                t.from = dataComponent.outputNodes[t.from].getSource();
            }
        }
    }
    // inline values for datasets that are in the datastore
    for (const d of data) {
        if (d.name in datasets) {
            d.values = datasets[d.name];
        }
    }
    return data;
}
//# sourceMappingURL=assemble.js.map