class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # output the max width of a binary tree
        # re-assign the value of the node
        if root == None:
            return 0

        root.val = 1
        queue = [root]
        left = 1
        right = 1
        width = 0
        while (len(queue)>0):
            size = len(queue) # queue stores the nodes of each level
            for i in range(size):
                cur = queue.pop(0)
                if i == 0:
                    left = cur.val
                if i == size-1:
                    right = cur.val
                if cur.left != None:
                    cur.left.val = cur.val * 2
                    queue.append(cur.left)
                if cur.right != None:
                    cur.right.val = cur.val * 2 + 1
                    queue.append(cur.right)
                
                width = max(width, right - left + 1)
        return width