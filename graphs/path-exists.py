# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex start to vertex end.

# Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited = {}
        queue = deque([start])
        found = False
        while bool(queue):
            start = queue[0]
            for v1,v2 in edges:          
                if (v1 == start) and (v2 not in visited.keys()):
                        queue.append(v2)
                if (v2 == start) and (v1 not in visited.keys()):
                        queue.append(v1)
            q = queue.popleft()
            if q == end:
                found = True
                return True
            elif q not in visited.keys(): 
                visited[q] = True
            else: 
                continue