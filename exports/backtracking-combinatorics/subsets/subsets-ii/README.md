---
export_schema_version: 1
id: 2dbad318-797a-4996-a5ba-26f236e1dfd0
source: leetcode
source_key: subsets-ii
slug: subsets-ii
title: Subsets II
url: https://leetcode.com/problems/subsets-ii/
difficulty: Medium
status: Understood
primary_subtag_id: dc94b58c-a6b1-5faa-bf91-b345d4dd0abe
primary_path:
- backtracking-combinatorics
- subsets
taxonomy_ids:
- e3559c87-88b2-5555-8d01-abcf125b8845
- 0ced7452-092a-5352-b714-ad0f03bba12e
time_complexity: O(n log n + n × unique subsets)
space_complexity: O(n) auxiliary + output
created_at: '2026-08-27T19:49:12.715623Z'
updated_at: '2026-08-31T13:14:44.038758Z'
mistake_events:
- id: 0e8e4473-d8cf-4978-b4ae-915bb8c17d3f
  occurred_at: '2026-08-27T19:49:12.715949Z'
  observation: A global seen set removed duplicates only after generating them.
  reason_ids:
  - 3880238c-fdff-5e59-ae56-425ea59658a3
  - de0ada30-5a0b-5e9e-b4ab-482c3ce38856
---

# Subsets II

[Open on Leetcode](https://leetcode.com/problems/subsets-ii/)

## Why I missed it

- The duplicate condition was treated globally instead of relative to one recursion level.

## Recognition signals

- Equal sorted values create identical sibling branches, but equal values at deeper levels represent additional copies.

## Core insight

- Same value plus same recursion level means skip; same value at a deeper level is allowed.

## Approach

- Sort so duplicate candidates are adjacent.
- Record the current path immediately.
- At each level, skip an equal value unless it is the first candidate for that level.
- Choose, recurse with the next index, and remove.

## Invariants

- Chosen indices strictly increase and no recursion level starts two branches with the same value.

## Edge cases

- All values equal.
- No duplicates.
- Empty input.
- Several duplicate groups.

## Follow-up

- Relate the number of visited states to the number of unique subsets rather than only 2^n.
