class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # this question needs to use index
        # postorder: left, right ,root
        # inorder: left, root, right
        # the last one of postorder is root, and root divides the inorder into left tree nodes and right tree nodes
        if inorder==postorder==[]:
            return
             
        def solver(istart, iend, pstart, pend):
            if istart >= iend or pstart >= pend:
                return
            val = postorder[pend-1]
            node = TreeNode(val)
            iroot = inorder.index(val)
            
            node.left = solver(istart, iroot, pstart, pstart + iroot - istart) 
            node.right = solver(iroot + 1, iend, pstart + iroot - istart, pend - 1) # pstart pend: postorder, iroot iend inorder 
            return node
        
        
        len1 = len(inorder)
        return solver(0,len1,0,len1)
        