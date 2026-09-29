---
export_schema_version: 1
id: e2f9972d-8f97-478b-80cc-2ce9f928cecb
source: leetcode
source_key: is-graph-bipartite
slug: is-graph-bipartite
title: Is Graph Bipartite?
url: https://leetcode.com/problems/is-graph-bipartite/
difficulty: Medium
status: Resolved
primary_subtag_id: 7d7e497f-144a-59d4-8e11-b32387bfeca4
primary_path:
- graphs-networks
- graph-traversal
taxonomy_ids:
- e8114580-e74d-59ce-b475-c6f34e6a49f7
- 054ef9fe-949a-55b2-9bda-92b17b4d682f
time_complexity: O(V + E)
space_complexity: O(V)
created_at: '2026-08-27T19:49:12.706342Z'
updated_at: '2026-08-28T01:47:14.867179Z'
mistake_events:
- id: 552be431-11f7-42ba-a16f-704e519052b7
  occurred_at: '2026-08-27T19:49:12.706675Z'
  observation: The first attempt tied colors to BFS levels and did not safely handle
    disconnected components.
  reason_ids:
  - 30cd7713-9098-546b-b0cb-36625f6d969b
  - 68ac55cb-6c3e-5f03-8cf2-e0768cb6b4c8
---

# Is Graph Bipartite?

[Open on Leetcode](https://leetcode.com/problems/is-graph-bipartite/)

## Why I missed it

- Tracked traversal level instead of preserving one color per vertex across the whole component.

## Recognition signals

- Every edge requires its endpoints to belong to opposite groups.

## Core insight

- Color an unvisited neighbor opposite the current node; reject an edge whose endpoints already share a color.

## Approach

- Start a traversal from every still-uncolored vertex.
- Seed either color.
- Color new neighbors with the opposite value.
- Stop on a same-color edge.

## Invariants

- Every processed edge joins opposite colors.

## Edge cases

- Disconnected graph.
- Isolated vertex.
- Odd cycle.
- Even cycle.

## Follow-up

- Recognize odd-cycle detection as the same invariant.
