import type { D3Element } from '../../mermaidAPI.js';
import type { FilledMindMapNode, MindmapDB } from './mindmapTypes.js';
import type { MermaidConfig } from '../../config.type.js';
/**
 * @param db - The database
 * @param elem - The D3 dom element in which the node is to be added
 * @param node - The node to be added
 * @param fullSection - ?
 * @param conf - The configuration object
 * @returns The height nodes dom element
 */
export declare const drawNode: (db: MindmapDB, elem: D3Element, node: FilledMindMapNode, fullSection: number, conf: MermaidConfig) => number;
export declare const positionNode: (db: MindmapDB, node: FilledMindMapNode) => void;
