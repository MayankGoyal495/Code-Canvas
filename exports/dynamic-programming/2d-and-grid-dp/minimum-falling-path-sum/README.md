---
export_schema_version: 1
id: b6b055cb-2349-473f-bf0e-5cc80879048e
source: leetcode
source_key: minimum-falling-path-sum
slug: minimum-falling-path-sum
title: Minimum Falling Path Sum
url: https://leetcode.com/problems/minimum-falling-path-sum/
difficulty: Medium
status: Understood
primary_subtag_id: 68a852bb-0f40-5a18-b469-23c7013a6b9a
primary_path:
- dynamic-programming
- 2d-and-grid-dp
taxonomy_ids:
- 880edbfd-20b6-5198-a766-5232b888276a
- acd97bba-08f3-5641-9de0-8afd44b319ae
- a3299138-878c-5ba6-bdd5-51ef90c513d7
time_complexity: O(rows × columns)
space_complexity: O(rows × columns)
created_at: '2026-08-27T19:49:12.697014Z'
updated_at: '2026-08-28T01:03:48.519572Z'
mistake_events:
- id: 4064718e-0577-4412-b8ee-263bcbd05adc
  occurred_at: '2026-08-27T19:49:12.697353Z'
  observation: Needed a clear top-down state, base row, and the three legal next pointers.
  reason_ids:
  - 30cd7713-9098-546b-b0cb-36625f6d969b
  - db65a4d5-7438-5bb6-a851-ce9c1700d197
---

# Minimum Falling Path Sum

[Open on Leetcode](https://leetcode.com/problems/minimum-falling-path-sum/)

## Why I missed it

- The recurrence was easier to state than the pointer bounds and row/column order.

## Recognition signals

- Movement is acyclic from one row to the next and each cell has only three possible continuations.

## Core insight

- State means the minimum sum starting at one cell; the last row is the base case.

## Approach

- Seed the last row with its own values.
- Move upward and read only down-left, down, and down-right cells that exist.
- Add the current cell to the cheapest child.
- Take the minimum value in the top row.

## Invariants

- The entire child row is resolved before a parent row uses it.

## Edge cases

- Single cell.
- Negative values.
- Left and right columns have only two legal children.

## Follow-up

- Compress space to one row after the 2D state is intuitive.
