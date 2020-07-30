class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # from bottom to up, left to right
        res = []
        level = 0
        self.dfs(root, res, level)
        return res[::-1]
    
    def dfs(self, node, res, level):
        if node == None:
            return
        if len(res) < level + 1:
            res.append([node.val]) # extend the length of res
        else:
            res[level].append(node.val)
        self.dfs(node.left, res, level+1)
        self.dfs(node.right, res, level+1)
        
        
        
        
        
        '''
        # non-recursion method
        if not root:
            return []
        queue = [root]
        answer = [[root.val]]
        while queue:
            child = []
            for node in queue:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            if not child: #last level of tree.
                break
            queue = child #assigning this level to queue.
            answer.append([node.val for node in queue])

        return answer[::-1]'''
