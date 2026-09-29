---
export_schema_version: 1
id: 6284537b-823e-4ed5-ad6f-a28129c54f1f
source: leetcode
source_key: palindrome-partitioning-ii
slug: palindrome-partitioning-ii
title: Palindrome Partitioning II
url: https://leetcode.com/problems/palindrome-partitioning-ii/description/
difficulty: Hard
status: Resolved
primary_subtag_id: 7446323a-ffc4-5c02-a36c-107167ee0510
primary_path:
- dynamic-programming
- 1d-dp
taxonomy_ids:
- acd97bba-08f3-5641-9de0-8afd44b319ae
- 843daa45-ee26-5bef-92fb-7a2723b8ae97
- 6518e5af-27ca-57ea-ab6a-fd6b73954026
time_complexity: O(n^2)
space_complexity: O(n^2)
created_at: '2026-08-24T18:12:15.562015Z'
updated_at: '2026-08-24T18:12:15.696026Z'
mistake_events:
- id: c0bb7566-a611-4a0c-ae60-dafa2065db2f
  occurred_at: '2026-08-24T18:12:15.569389Z'
  observation: 'Attempt 1: interval recursion explored every split without a viable
    state reduction and timed out.'
  reason_ids:
  - 3880238c-fdff-5e59-ae56-425ea59658a3
- id: 8eeda70e-4e25-4c39-98aa-e1bbb47deb5f
  occurred_at: '2026-08-24T18:12:15.618505Z'
  observation: 'Attempt 2: memoized solve(i, j) had O(n^2) states and O(n) split work
    per state, so O(n^3) still timed out for n = 2000.'
  reason_ids:
  - 3880238c-fdff-5e59-ae56-425ea59658a3
- id: 557b2815-c9dc-4765-b773-ac4cbb28e1db
  occurred_at: '2026-08-24T18:12:15.665900Z'
  observation: 'Attempt 3: checked palindrome[end][start] and added cuts[end - 1]
    instead of palindrome[start][end] and cuts[start - 1]; Wrong Answer on cdd.'
  reason_ids:
  - 30cd7713-9098-546b-b0cb-36625f6d969b
- id: 76dd9194-cc32-4c70-99d4-5205b02f2fd7
  occurred_at: '2026-08-24T18:12:15.695575Z'
  observation: 'Attempt 4: printed the O(n^2) palindrome table and hit Output Limit
    Exceeded even after the recurrence was corrected.'
  reason_ids:
  - 6ce88eae-67d8-5665-b266-e231c383bd20
---

# Palindrome Partitioning II

[Open on Leetcode](https://leetcode.com/problems/palindrome-partitioning-ii/description/)

## Why I missed it

- Memoizing solve(i, j) still leaves O(n^2) interval states with O(n) split work per state: O(n^3).
- Read the palindrome table backwards as palindrome[end][start] instead of palindrome[start][end].
- Used cuts[end - 1] instead of cuts[start - 1], so the transition ignored where the final palindrome began.
- Left print(palindrome) in an O(n^2) solution and triggered Output Limit Exceeded.

## Recognition signals

- Minimum cuts over a prefix plus fast validity checks for every substring suggests precompute + prefix DP.
- When the transition asks where the final valid segment starts, prefer a 1D prefix state over solving both interval halves.

## Core insight

- Precompute palindrome[start][end], then choose the start of the final palindrome for each prefix ending at end.
- Always calculate DP cost as number of states multiplied by work per state; memoization alone does not guarantee speed.

## Approach

- Fill the palindrome table with start decreasing so palindrome[start + 1][end - 1] is already known.
- Set cuts[end] = 0 when s[0:end+1] is a palindrome.
- Otherwise try every start from 1 through end and minimize cuts[start - 1] + 1 when s[start:end+1] is a palindrome.

## Invariants

- palindrome[start][end] is meaningful only when start <= end; the useful table is on or above the diagonal.
- Before computing cuts[end], every smaller prefix cut value is already optimal.
- Each transition appends exactly one verified palindrome s[start:end+1].

## Edge cases

- A single character or an entirely palindromic string needs zero cuts.
- Adjacent equal characters are a palindrome without consulting an inner interval.
- Handle start = 0 through the whole-prefix branch so cuts[-1] is never used.

## Follow-up

- An alternative center-expansion formulation keeps O(n^2) time while reducing auxiliary space to O(n).
- Remove table-sized debug output before submitting.
