---
export_schema_version: 1
id: f6ad1adb-fc4f-4311-abb5-80cd1cd1225c
source: leetcode
source_key: '1268'
slug: search-suggestions-system
title: Search Suggestions System
url: https://leetcode.com/problems/search-suggestions-system/
difficulty: Medium
status: Resolved
primary_subtag_id: ab3483bd-3a44-5c2d-928f-deb4d858795f
primary_path:
- trees-ordered
- tries
taxonomy_ids:
- c9a30ffd-f175-5192-950a-862bb955d3df
- 6518e5af-27ca-57ea-ab6a-fd6b73954026
time_complexity: O(S + q² + qL)
space_complexity: O(S)
created_at: '2026-08-31T13:54:16.322954Z'
updated_at: '2026-08-31T13:54:16.322958Z'
mistake_events:
- id: 017c2813-70cb-4882-a165-772d6e5fb0b0
  occurred_at: '2026-08-31T13:54:16.328122Z'
  observation: ''
  reason_ids: []
---

# Search Suggestions System

[Open on Leetcode](https://leetcode.com/problems/search-suggestions-system/)

## Why I missed it

- I found the trie node for each prefix, but missed the second stage: DFS through that node's descendants to collect suggestions.
- I needed to append a terminal product before exploring child edges, traverse children alphabetically, and stop after three results.
- A fresh temporary result list is required for every prefix, and list.sort() mutates in place instead of returning a sorted list.
