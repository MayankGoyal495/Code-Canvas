---
export_schema_version: 1
id: 588a7d5b-acff-4fb7-ba4e-6908f0af23dd
source: leetcode
source_key: maximal-square
slug: maximal-square
title: Maximal Square
url: https://leetcode.com/problems/maximal-square/
difficulty: Medium
status: Resolved
primary_subtag_id: 68a852bb-0f40-5a18-b469-23c7013a6b9a
primary_path:
- dynamic-programming
- 2d-and-grid-dp
taxonomy_ids:
- acd97bba-08f3-5641-9de0-8afd44b319ae
- a3299138-878c-5ba6-bdd5-51ef90c513d7
time_complexity: O(m × n)
space_complexity: O(m × n)
created_at: '2026-08-28T03:07:24.049692Z'
updated_at: '2026-08-28T03:07:24.049697Z'
mistake_events:
- id: 991b676d-3d7e-431f-8e22-a18775713dd8
  occurred_at: '2026-08-28T03:07:24.051384Z'
  observation: Accepted, then simplified by letting min() handle zero neighbors and
    initializing the skipped boundaries directly.
  reason_ids:
  - 30cd7713-9098-546b-b0cb-36625f6d969b
  - db65a4d5-7438-5bb6-a851-ce9c1700d197
---

# Maximal Square

[Open on Leetcode](https://leetcode.com/problems/maximal-square/)

## Why I missed it

- The first row and first column were skipped by the recurrence loop, so they needed explicit initialization.
- Added a redundant condition requiring all three neighbors to be nonzero before applying the recurrence.

## Recognition signals

- The largest square ending at a cell depends only on its top, left, and top-left neighbors.

## Core insight

- For a 1-cell, its largest square side is 1 plus the minimum neighboring side; a zero neighbor naturally reduces it to a 1×1 square.

## Approach

- Convert the string matrix to integer DP values.
- Initialize the maximum from the first row and first column because the interior loop skips them.
- For each interior 1-cell, apply 1 + min(diagonal, top, left).
- Track the maximum side and return its square as the area.

## Invariants

- dp[i][j] is the side length of the largest all-1 square whose bottom-right corner is (i, j).

## Edge cases

- A single-cell matrix.
- All zeros.
- The only 1 lies in the first row or first column.
- A zero neighbor limits the current square to side length one.

## Follow-up

- Compress the DP to one row while preserving the previous diagonal value.
