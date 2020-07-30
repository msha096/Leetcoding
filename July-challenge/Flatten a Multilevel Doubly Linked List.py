class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        s = []
        if head==[]:
            return []
        node = head
        count = 0
        while node:            
            if node.child:        
                if node.next:
                    s.append(node.next)
                node.next = node.child
                if node.next:
                    node.next.prev = node
                node.child = None
                
            elif node.next == None and len(s)>0:
                node.next = s.pop(-1)
                if node.next:
                    node.next.prev = node # should set the prev after change .next, since it is double linked.
            node = node.next
                
                    
        return head