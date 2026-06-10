class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        n = len(nums)

        # Build log table
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        m = lg[n] + 1

        # Sparse tables
        mx = [[0] * m for _ in range(n)]
        mn = [[0] * m for _ in range(n)]

        for i in range(n):
            mx[i][0] = nums[i]
            mn[i][0] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            for i in range(n - length + 1):
                mx[i][j] = max(mx[i][j - 1],
                               mx[i + half][j - 1])

                mn[i][j] = min(mn[i][j - 1],
                               mn[i + half][j - 1])
            j += 1

        def query_max(l, r):
            p = lg[r - l + 1]
            return max(mx[l][p], mx[r - (1 << p) + 1][p])

        def query_min(l, r):
            p = lg[r - l + 1]
            return min(mn[l][p], mn[r - (1 << p) + 1][p])

        # Max heap using negative values
        heap = []

        for l in range(n):
            val = query_max(l, n - 1) - query_min(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))

        ans = 0

        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            val = -val

            ans += val

            if r > l:
                nxt = query_max(l, r - 1) - query_min(l, r - 1)
                heapq.heappush(heap, (-nxt, l, r - 1))

        return ans
        
