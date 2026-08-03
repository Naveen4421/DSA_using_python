class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i]: best score diff from index i onward
        
        for i in range(n - 1, -1, -1):
            take = 0
            dp[i] = float('-inf')
            for k in range(1, 4):
                if i + k - 1 < n:
                    take += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], take - dp[i + k])
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
