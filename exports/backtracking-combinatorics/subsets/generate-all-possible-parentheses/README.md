---
export_schema_version: 1
id: b7d3a194-15ab-4578-b37a-b196a8a7e8f0
source: geeksforgeeks
source_key: generate-all-possible-parentheses
slug: generate-all-possible-parentheses
title: Generate Parentheses
url: https://www.geeksforgeeks.org/problems/generate-all-possible-parentheses/1
difficulty: Medium
status: Resolved
primary_subtag_id: dc94b58c-a6b1-5faa-bf91-b345d4dd0abe
primary_path:
- backtracking-combinatorics
- subsets
taxonomy_ids:
- e3559c87-88b2-5555-8d01-abcf125b8845
time_complexity: O(C(n/2) × n)
space_complexity: O(n) auxiliary + output
created_at: '2026-08-28T02:16:58.279818Z'
updated_at: '2026-09-01T13:14:52.131625Z'
mistake_events:
- id: 7cd5284b-9b80-41ca-bec8-9a8168a90ad4
  occurred_at: '2026-08-28T02:16:58.280224Z'
  observation: 'Solved successfully on the first submission: 22/22 test cases passed.'
  reason_ids: []
---

# Generate Parentheses

[Open on Geeksforgeeks](https://www.geeksforgeeks.org/problems/generate-all-possible-parentheses/1)

## Why I missed it

- No recorded miss; the submission passed all test cases on the first attempt.

## Recognition signals

- Build a constrained sequence one character at a time and reject a prefix as soon as it cannot become valid.

## Core insight

- A valid prefix never has more closing than opening parentheses, and a completed answer has equal counts.

## Approach

- Start with one opening parenthesis.
- Prune when closed exceeds opened or the string exceeds n characters.
- Record a string at length n only when both counts match.
- Otherwise try appending an opening and a closing parenthesis.

## Invariants

- Every explored prefix has opened at least closed and never exceeds the target length.

## Edge cases

- The smallest valid length n=2.
- A closing parenthesis cannot be the first character.
- Only even target lengths can finish with equal counts.

## Follow-up

- Compare this total-length formulation with APIs where n means the number of pairs.
