# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children 
# is separated by the null value (See examples).

# https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3897/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None: 
            return []
        
        
        queue_of_nodes = deque([root])    
        result = []
        while queue_of_nodes:
            level = []
            for _ in range(len(queue_of_nodes)):
                node = queue_of_nodes.popleft()
                level.append(node.val)
                queue_of_nodes.extend(node.children) #we use extend so we the values at the same level are not separated
            result.append(level)
        return result 