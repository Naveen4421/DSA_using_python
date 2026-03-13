def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=pre
            pre=curr
            curr=temp
        return pre
