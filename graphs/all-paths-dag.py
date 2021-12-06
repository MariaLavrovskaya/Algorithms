# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        if len(graph) == 0 or not graph:
            return paths
        
        queue = deque()
        queue.append([0])
        
        while queue:
            # We take the full path
            current_path = queue.popleft()
            # By definition of the problem, the number of nodes is n, so by accessing the last element 
            # of the current we grab the vertex we are at 
            node = current_path[-1]
            for next_node in graph[node]:
                temp_path = current_path.copy()
                temp_path.append(next_node) #we construct a full path
            
                if next_node == len(graph) - 1: #if the length of the path is n-1, that means we reached a final node
                    paths.append(temp_path)
                else:
                    queue.append(temp_path) #else we need to add the element as it is not a final element
        
        return paths