---
export_schema_version: 1
id: 940ddbe1-a81b-4bcb-8b14-754e989792cf
source: leetcode
source_key: koko-eating-bananas
slug: koko-eating-bananas
title: Koko Eating Bananas
url: https://leetcode.com/problems/koko-eating-bananas/
difficulty: Medium
status: Understood
primary_subtag_id: 6b178111-6da6-534e-aeef-97c0915531f4
primary_path:
- search-ordering
- binary-search
taxonomy_ids:
- 47e633cf-4410-5fe3-938e-8a2954994c67
time_complexity: O(n log max(piles))
space_complexity: O(1)
created_at: '2026-08-27T19:49:12.677170Z'
updated_at: '2026-08-28T01:03:48.499491Z'
mistake_events:
- id: ac38e2e3-076f-436c-96bd-eb79a5f0002f
  occurred_at: '2026-08-27T19:49:12.677581Z'
  observation: The feasibility calculation used a hard-coded divisor and shadowed
    the candidate parameter.
  reason_ids:
  - 30cd7713-9098-546b-b0cb-36625f6d969b
  - 6ce88eae-67d8-5665-b266-e231c383bd20
---

# Koko Eating Bananas

[Open on Leetcode](https://leetcode.com/problems/koko-eating-bananas/)

## Why I missed it

- Mixed up the candidate answer with an array position and did not consistently test the current midpoint.

## Recognition signals

- The question asks for a minimum integer rate and feasibility becomes easier as the rate increases.

## Core insight

- Binary-search the first speed whose total required hours is at most h.

## Approach

- Bound the speed from 1 through the largest pile.
- Evaluate one midpoint by summing ceiling divisions.
- Keep the midpoint when feasible because it may be the first valid speed; otherwise discard it and every slower speed.

## Invariants

- The answer always remains inside the current inclusive interval.

## Edge cases

- One pile.
- h equals the number of piles.
- Very large piles where floating-point ceiling should be avoided.

## Follow-up

- Practice naming the monotonic predicate before choosing boundary updates.
