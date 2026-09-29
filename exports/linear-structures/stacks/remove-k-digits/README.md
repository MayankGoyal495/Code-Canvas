---
export_schema_version: 1
id: 1fd7f8a2-c015-4c65-ac9c-07173af4d6f2
source: leetcode
source_key: remove-k-digits
slug: remove-k-digits
title: Remove K Digits
url: https://leetcode.com/problems/remove-k-digits/description/
difficulty: Medium
status: Resolved
primary_subtag_id: cdcd2e43-2dd4-5dc7-b780-43650c33e9f9
primary_path:
- linear-structures
- stacks
taxonomy_ids:
- 61d24c1f-b41c-5e63-988d-68e58e3c051b
- 6518e5af-27ca-57ea-ab6a-fd6b73954026
time_complexity: O(n^2) portable worst case; O(n) stack processing
space_complexity: O(n)
created_at: '2026-09-07T01:31:44.365073Z'
updated_at: '2026-09-07T01:31:44.365085Z'
mistake_events: []
---

# Remove K Digits

[Open on Leetcode](https://leetcode.com/problems/remove-k-digits/description/)

## Recognition signals

- Removing digits while preserving order suggests greedy prefix decisions backed by a monotonic stack.

## Core insight

- Spend removals on a larger preceding digit when a smaller incoming digit can improve the earliest differing position.

## Approach

- Return zero if every digit must be removed.
- Scan left to right: pop larger predecessors while k remains, then append the current index.
- Spend leftover removals at the stack tail, assemble res from retained indexes, then trim leading zeros.

## Invariants

- Stack entries are original indexes in increasing order; repeated digits retain distinct identities.
- Each pop consumes one removal when the following k decrement executes. Zero formatting does not consume k.
- Equal digits do not satisfy the strict > comparison. After k reaches zero, the retained digit sequence may descend.

## Edge cases

- Remove every digit; equal digits; increasing digits requiring tail cleanup; budget exhausted before scanning finishes.
- Leading zeros and all-zero retained output must normalize correctly to a string, including "0".

## Follow-up

- Stack operations are O(n): each index is appended once and popped at most once. Repeated res += num[digit] has portable worst-case O(n^2) copying cost.
- Use "".join(num[index] for index in stack) for guaranteed linear output construction; retain O(n) auxiliary space.
