---
export_schema_version: 1
id: 751b821a-431c-423c-8a80-02b4224d8e15
source: leetcode
source_key: ipo
slug: ipo
title: IPO
url: https://leetcode.com/problems/ipo/
difficulty: Hard
status: Understood
primary_subtag_id: 767f64cc-a1b6-5274-bc8d-33da0a9c66c6
primary_path:
- trees-ordered
- heaps
taxonomy_ids:
- b4793eb3-4749-52d0-a3cf-c1b39dc4b34d
- 0ced7452-092a-5352-b714-ad0f03bba12e
time_complexity: O(n log n + k log n)
space_complexity: O(n)
created_at: '2026-08-27T19:49:12.733886Z'
updated_at: '2026-08-28T01:03:48.546108Z'
mistake_events:
- id: 76c2e158-c309-4e53-987b-7cf72c64c261
  occurred_at: '2026-08-27T19:49:12.734346Z'
  observation: A single profit heap repeatedly popped and reinserted the same unaffordable
    project.
  reason_ids:
  - 3880238c-fdff-5e59-ae56-425ea59658a3
  - de0ada30-5a0b-5e9e-b4ab-482c3ce38856
---

# IPO

[Open on Leetcode](https://leetcode.com/problems/ipo/)

## Why I missed it

- One heap was asked to answer two incompatible orderings: affordability by capital and desirability by profit.

## Recognition signals

- Choices unlock over time according to one key, but the greedy choice uses another key.

## Core insight

- Move every newly affordable project from a capital ordering into a maximum-profit ordering, then take the best available profit.

## Approach

- Order locked projects by required capital.
- For each round, unlock every project affordable with current w.
- Stop if the profit structure is empty.
- Choose its maximum and add that profit to w.

## Invariants

- The profit structure contains all and only affordable unchosen projects.

## Edge cases

- Nothing is initially affordable.
- All projects are initially affordable.
- k exceeds the number of useful projects.
- Several projects share a capital requirement.

## Follow-up

- State the exchange argument: a larger available profit cannot reduce future options.
