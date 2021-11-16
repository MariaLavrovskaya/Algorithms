# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         Case 2. Where there is no root value
        if root == None:
            return []
#         Case 1. Where there is only one root and no leaves
        if root.left == None and root.right == None:
            return [root.val]
        preorder = []
        not_visited = []
        current = root
        while current:
            preorder.append(current.val)
            if current.right:
                not_visited.append(current.right)
            if current.left:
                current = current.left
            elif current.left == None and len(not_visited) > 0:
                current = not_visited[-1]
                not_visited.pop(-1)
            else:
                break
        return preorder