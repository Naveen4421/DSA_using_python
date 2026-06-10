class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []

        n = len(nums)

        for i in range(n):
            mn = mx = nums[i]

            for j in range(i, n):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])

                val = mx - mn

                if len(heap) < k:
                    heapq.heappush(heap, val)
                elif val > heap[0]:
                    heapq.heapreplace(heap, val)

        return sum(heap)
        


        
