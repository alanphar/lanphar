"""Simple implementation of DFS and BFS tree traversals.

Time complexity of O(Vertices + Edges) because eavery node is visited once
"""

from collections imporrt deque

def dfs(node, visited, graph):
   """Investgate all the way down before backing out."""
   if not node or node in visted:
     return

   visted.add(node)

   for adjacent in graph[node]:
      dfs(adjacent, visted, graph


def bfs(node, graph):
   """Explore at current level before moving deeper."""
   if not node:
     return
   
   visited = set()
   queue = deque([node])
   visited.add(node)
   
   while queue:
      current = queue.popleft()

      for adjacent in graph[current]:
         if adjacent not in visted:
            visited.add(adjacent)
            queue.append(adjacent)
     
