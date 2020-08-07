# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return 
        #d = {0:[(0, root.val)]} # value: priority queue
        d = {}
       
        def dfs(node, x, y):
            if node.val!=None:
                if x in d:
                    heapq.heappush(d[x], (y, node.val))
                else: 
                    d[x] = [(y, node.val)]
            if node.left:
                dfs(node.left, x-1, y+1)
                
            if node.right:
                dfs(node.right, x+1, y+1)
                
        dfs(root,0,0)
        #print(d)
        k = [key for key in d]
        k.sort()
        
        res = [[] for i in range(len(k))]
        for i in range(len(k)):
            while d[k[i]]:
                res[i].append(heapq.heappop(d[k[i]])[1])
        return res