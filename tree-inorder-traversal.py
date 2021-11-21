# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         Case 1. Where there is no root node
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        inorder = []
        not_visited = []
        current = root
        while current or not_visited:
            while current:
                not_visited.append(current)
                current = current.left
            current = not_visited.pop(-1)
            inorder.append(current.val)
            current = current.right
        return inorder
