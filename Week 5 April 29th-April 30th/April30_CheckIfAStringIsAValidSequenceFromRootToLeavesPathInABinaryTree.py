# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if len(arr)==1 and root.val==arr[0]:
            if root.right==None and root.left==None:
                return True
            else:
                return False
        if root.val==arr[0]:
            #go ahead
            left = False
            right = False
            if root.left!=None:
                if root.left.val==arr[1]:
                    left = self.isValidSequence(root.left,arr[1:])
            if root.right!=None:
                if root.right.val==arr[1]:
                    right = self.isValidSequence(root.right,arr[1:])
            if left==True or right==True:
                return True
        return False