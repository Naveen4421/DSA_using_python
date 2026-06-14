# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)
        ans = 0

        for i in range(n // 2):
            ans = max(ans, arr[i] + arr[n - 1 - i])

        return ans



        
