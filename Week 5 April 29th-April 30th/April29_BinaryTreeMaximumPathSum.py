# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.m = float('-inf')
        
        def find_path_sum(root):
            
            if root is None:
                return 0
            
            else:
                left = max(find_path_sum(root.left), 0)
                right = max(find_path_sum(root.right), 0)
                self.m = max(self.m, left + right + root.val)
                return max(left, right, 0) + root.val
        
        find_path_sum(root)
        return self.m