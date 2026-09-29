---
export_schema_version: 1
id: ae551e91-1e3d-4ccb-8b10-c20d6b45c68d
source: leetcode
source_key: matchsticks-to-square
slug: matchsticks-to-square
title: Matchsticks to Square
url: https://leetcode.com/problems/matchsticks-to-square/description/
difficulty: Medium
status: Resolved
primary_subtag_id: e3559c87-88b2-5555-8d01-abcf125b8845
primary_path:
- backtracking-combinatorics
- constraint-search
taxonomy_ids:
- 054ef9fe-949a-55b2-9bda-92b17b4d682f
- 0ced7452-092a-5352-b714-ad0f03bba12e
time_complexity: O(4^n) worst case
space_complexity: O(n) auxiliary space
created_at: '2026-09-06T14:19:53.254919Z'
updated_at: '2026-09-06T14:19:53.254924Z'
mistake_events:
- id: 5f7d1b44-28f2-446f-80ba-23461e3a731f
  occurred_at: '2026-09-06T00:00:00Z'
  observation: 'Retrospective: I returned the first fitting recursive branch immediately
    after it failed, so sibling sides were never explored.'
  reason_ids:
  - 30cd7713-9098-546b-b0cb-36625f6d969b
  - 6ce88eae-67d8-5665-b266-e231c383bd20
---

# Matchsticks to Square

[Open on Leetcode](https://leetcode.com/problems/matchsticks-to-square/description/)

## Why I missed it

- Returning a failed first fitting branch skipped the remaining side choices.

## Recognition signals

- When items must be assigned to groups and an early legal choice can block later assignments, recognize backtracking.

## Core insight

- Return immediately on success; after a child returns False, continue exploring the next legal side.

## Approach

- Compute the target, reject non-divisible totals, sort largest-first, and explore left, right, top, and down.

## Invariants

- Assigned-prefix totals are conserved; no side exceeds target; scalar parent arguments remain unchanged after a child returns.

## Edge cases

- Non-divisible totals, a stick larger than target, repeated lengths, and divisible totals with no valid assignment.

## Follow-up

- A max-stick guard and symmetry pruning are useful optimizations, but they are intentionally separate from the saved implementation.
