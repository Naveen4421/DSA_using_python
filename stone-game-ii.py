class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            if i >= n:
                return 0
            if 2 * M >= n - i:
                return suffix[i]
            key = (i, M)
            if key in memo:
                return memo[key]
            best = 0
            for X in range(1, 2 * M + 1):
                gained = suffix[i] - dp(i + X, max(M, X))
                if gained > best:
                    best = gained
            memo[key] = best
            return best

        return dp(0, 1)
