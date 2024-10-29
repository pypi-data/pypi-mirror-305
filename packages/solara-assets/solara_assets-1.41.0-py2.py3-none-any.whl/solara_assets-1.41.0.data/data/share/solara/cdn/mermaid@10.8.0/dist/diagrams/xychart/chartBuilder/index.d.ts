import type { Group } from '../../../diagram-api/types.js';
import type { DrawableElem, XYChartConfig, XYChartData, XYChartThemeConfig } from './interfaces.js';
export declare class XYChartBuilder {
    static build(config: XYChartConfig, chartData: XYChartData, chartThemeConfig: XYChartThemeConfig, tmpSVGGroup: Group): DrawableElem[];
}
