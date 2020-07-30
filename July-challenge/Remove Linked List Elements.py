class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None and head.val == val:
            head = head.next
        node = head
        if head == None:
            return None
        while node.next != None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head