# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        prev, cur = head, head.next
        idx = 1
        first = last = -1
        min_dist = float('inf')

        while cur.next:
            is_critical = (
                (cur.val > prev.val and cur.val > cur.next.val) or
                (cur.val < prev.val and cur.val < cur.next.val)
            )
            if is_critical:
                if first == -1:
                    first = idx
                else:
                    min_dist = min(min_dist, idx - last)
                last = idx
            prev, cur = cur, cur.next
            idx += 1

        if first == last:  
            return [-1, -1]
        return [min_dist, last - first]
        
