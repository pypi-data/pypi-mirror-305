import type { DiagramMetadata } from './diagram-api/types.js';
/**
 * Preprocess the given code by cleaning it up, extracting front matter and directives,
 * cleaning and merging configuration, and removing comments.
 * @param code - The code to preprocess.
 * @returns The object containing the preprocessed code, title, and configuration.
 */
export declare function preprocessDiagram(code: string): DiagramMetadata & {
    code: string;
};
