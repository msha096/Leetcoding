# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        '''# 40 faster
        if root == None:
            return 0
        node = root
        res = 0
        q = [node]
        
        def helper(node, cur, sum):
            if node == None:
                return 0
            else:
                cur += node.val       
                if cur == sum:
                    return 1 + helper(node.right,cur, sum) + helper(node.left,cur, sum) # same beginning node, can have more than 1 valid path
                else:
                    return helper(node.right,cur, sum)+helper(node.left,cur, sum)                        
             
        while q:
            size = len(q)
            for i in range(size):
                node = q.pop()
                res += helper(node,0,sum)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res'''
        '''# use prefix sum  97% faster
        d = defaultdict(int)
           
        res = 0
        if root == None:
            return 0
        
        def prefixSum(node, sum, prefixsum):
            nonlocal res
            if prefixsum == sum:
                res += 1
            if prefixsum - sum in d: # we have 18 now, and prev sum is 10, target is 8, then there is one path if cur_sum - target sum in the dict
                res += d[prefixsum-sum]
            d[prefixsum] += 1
            if node.left:
                prefixSum(node.left, sum, prefixsum + node.left.val)
            if node.right:
                prefixSum(node.right, sum, prefixsum + node.right.val)
            d[prefixsum] -= 1 # when we go up, we del by 1, backtracking key step
            if d[prefixsum] == 0:
                del d[prefixsum]
        
        prefixSum(root,sum,root.val)
        return res'''
        # use cumulative sum, method 2
        # if we have 10 now, with target 8, we need to find 10+8 in the deeper path
        # 95% faster
        if root is None:
            return 0
        res = 0
        d = defaultdict(int)
        d[sum] = 1 # pay attention
        def dfs(node, sum, cursum):
            if not node:
                return 
            cursum += node.val
            nonlocal res # python3 use nonlocal, python 2 use global
            res += d[cursum]
            d[cursum+sum] += 1
            dfs(node.left, sum, cursum)
            dfs(node.right, sum, cursum)
            d[cursum+sum] -= 1
        dfs(root,sum,0)
        return res
        
        