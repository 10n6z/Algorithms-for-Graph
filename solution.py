import graph

## THis is deliberately not implemented to allow you to implement it
# Because for this situation, there is no loops and all edges have the same weight or no weigth in this graph. Therefore, we just need
# to use BFS to find the shortest path instead of Djikstra's algorithm
def algorithm(g: graph.Graph, B, s:int, t:int) -> int:
  distances = {s: 0}
  b_counts = {s: 1 if s in B else 0}
  Q = [s]
    
  while Q:
    v = Q.pop(0)
    for u in g.adj[v]:
      if u not in distances:
        distances[u] = distances[v] + 1
        b_counts[u] = b_counts[v] + (1 if u in B else 0)
        Q.append(u)
      elif distances[v] + 1 == distances[u]:
        b_counts[u] = max(b_counts[u], b_counts[v] + (1 if u in B else 0))
    
  if t not in distances:
    return 0
    
  return b_counts.get(t, 0)
