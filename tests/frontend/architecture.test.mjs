import { test } from 'node:test';
import assert from 'node:assert/strict';
import { checkFrontend } from '../../scripts/check-architecture.mjs';
test('Architecture guard rejects shared-to-feature imports, deep cross-feature imports and runtime cycles', () => {
  const files = new Map([
    ['src/shared/wrong.ts', "import {x} from '../features/canvas/private'; export const y=x;"],
    ['src/features/canvas/private.ts', 'export const x=1;'],
    ['src/features/dashboard/page.ts', "import {x} from '../canvas/private';"],
    ['src/shared/a.ts', "import './b';"],
    ['src/shared/b.ts', "import './a';"],
    ['src/shared/styles/wrong.css', "@import '../../features/canvas/private.css';"],
    ['src/features/canvas/private.css', '.node { color: cyan; }'],
  ]);
  const errors = checkFrontend(files).join('\n');
  assert.match(errors, /shared code/);
  assert.match(errors, /public entry/);
  assert.match(errors, /Dependency cycle/);
  assert.match(errors, /wrong\.css: shared code/);
});
test('Architecture guard permits public feature entries and type-only reverse references', () => {
  const files = new Map([
    ['src/features/dashboard/page.ts', "import {x} from '../canvas';"],
    ['src/features/canvas/index.ts', "export {x} from './private';"],
    ['src/features/canvas/private.ts', 'export const x=1;'],
    ['src/shared/a.ts', "import type {B} from './b';export type A=B;"],
    ['src/shared/b.ts', "import type {A} from './a';export interface B{a?:A}"],
  ]);
  assert.deepEqual(checkFrontend(files), []);
});
