# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        if count==n:
            return head.next
        curr=head
        i=1
        while i<count-n:
            curr=curr.next
            i+=1
        curr.next=curr.next.next
        return head

        
