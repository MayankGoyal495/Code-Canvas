---
export_schema_version: 1
id: b72d8fc7-6a98-4508-9ac3-cdfd24f39ff1
source: leetcode
source_key: count-the-number-of-incremovable-subarrays-i
slug: count-the-number-of-incremovable-subarrays-i
title: Count the Number of Incremovable Subarrays I
url: https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/
difficulty: Easy
status: Understood
primary_subtag_id: 47e633cf-4410-5fe3-938e-8a2954994c67
primary_path:
- arrays-strings
- arrays
taxonomy_ids:
- eb56d27b-8767-58a3-92d0-580f4d92f4bc
time_complexity: O(n)
space_complexity: O(1)
created_at: '2026-08-29T18:51:46.817692Z'
updated_at: '2026-08-31T13:15:07.225293Z'
mistake_events:
- id: 590a1a67-961d-48f4-b482-ff62fa54f789
  occurred_at: '2026-08-29T18:51:46.833062Z'
  observation: Could not figure out the optimal solution; saved the brute-force approach
    for later review.
  reason_ids:
  - 3880238c-fdff-5e59-ae56-425ea59658a3
  - e47bcbb0-5c1b-5fad-a19e-3bbb8e6ee04a
---

# Count the Number of Incremovable Subarrays I

[Open on Leetcode](https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/)

## Why I missed it

- Enumerated every removed subarray and rebuilt the remainder instead of counting compatible increasing prefix/suffix boundaries.

## Recognition signals

- Removing one contiguous middle segment leaves only a prefix and a suffix.
- Both retained sides must be strictly increasing, and their boundary values must satisfy prefix_last < suffix_first.
- As the suffix start moves left, the compatible prefix pointer only needs to move left.

## Core insight

- Build the maximal increasing prefix, sweep an increasing suffix from right to left, and count all removal starts once the prefix/suffix bridge is valid.

## Approach

- Move i right to the end of the longest strictly increasing prefix.
- If i reaches n - 1, return n * (n + 1) // 2 because every non-empty subarray is removable.
- Initialize ans = i + 2 to count valid removals that end at n - 1.
- Move j left while nums[j:] remains strictly increasing.
- For each j, retreat i while nums[i] >= nums[j] so the retained prefix joins the suffix strictly.
- Add i + 2: removal start can be any index from 0 through i + 1.

## Invariants

- nums[0:i + 1] and nums[j:n] are strictly increasing.
- After the bridge loop, i < 0 or nums[i] < nums[j].
- i and j only move left during the suffix sweep, so their total movement is linear.

## Edge cases

- The whole array is already strictly increasing.
- The array is strictly decreasing.
- No prefix element can connect to the current suffix, so i becomes -1.
- A single-element array.

## Follow-up

- Replay the dedicated 2D trace and connect each highlighted rule to the matching Python line.
