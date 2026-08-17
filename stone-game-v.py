class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rangeSum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        val = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        for i in range(n):
            val[i][i] = stoneValue[i]
            maxL[i][i] = val[i][i]
            maxR[i][i] = val[i][i]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                total = rangeSum(i, j)

                lo, hi, pos = i, j - 1, j   # sentinel: "no split found" -> pos = j
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if 2 * rangeSum(i, mid) >= total:
                        pos = mid
                        hi = mid - 1
                    else:
                        lo = mid + 1

                best = 0
                if pos - 1 >= i:
                    cand = maxL[i][pos - 1]
                    if cand > best:
                        best = cand
                if pos + 1 <= j:
                    cand = maxR[pos + 1][j]
                    if cand > best:
                        best = cand
                if pos <= j - 1 and 2 * rangeSum(i, pos) == total:
                    cand = val[i][pos]
                    if cand > best:
                        best = cand

                dp[i][j] = best
                val[i][j] = total + best
                maxL[i][j] = max(maxL[i][j - 1], val[i][j])
                maxR[i][j] = max(maxR[i + 1][j], val[i][j])

        return dp[0][n - 1]
