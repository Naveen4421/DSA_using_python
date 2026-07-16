class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0
        for i, x in enumerate(nums):
            mx = max(mx, x)
            prefix_gcd[i] = gcd(x, mx)

        prefix_gcd.sort()

        total = 0
        lo, hi = 0, n - 1
        while lo < hi:
            total += gcd(prefix_gcd[lo], prefix_gcd[hi])
            lo += 1
            hi -= 1

        return total
