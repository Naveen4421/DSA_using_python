class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_right

        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1

        exact_count = [0] * (max_val + 1)

        for d in range(max_val, 0, -1):
            total = 0
            for multiple in range(d, max_val + 1, d):
                total += freq[multiple]
                exact_count[d] -= exact_count[multiple]
            exact_count[d] += total * (total - 1) // 2

        prefix = [0] * (max_val + 1)
        running = 0
        for d in range(max_val + 1):
            running += exact_count[d]
            prefix[d] = running

        return [bisect_right(prefix, q) for q in queries]
