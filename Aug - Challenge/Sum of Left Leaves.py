# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        '''def helper(node):
            res = 0
            if node == None:
                return res
            if node.left:
                if node.left.left ==node.left.right == None:
                    res = node.left.val              
            return res + helper(node.left) + helper(node.right)
            
        return helper(root)'''
        
        def dfs(node,side):
            if not node:
                return 
            if node.left == node.right == None:
                if side == -1:
                    self.sum += node.val
            dfs(node.left,-1)
            dfs(node.right,1)
        self.sum = 0
        dfs(root,0)
        return self.sum
        