# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.a = 1
        def dep(node):
            if not node:
                return 0
            left = dep(node.left)
            right = dep(node.right)
            self.a = max(left+right+1, self.a)
            return max(left, right) + 1

        dep(root)
        return self.a - 1