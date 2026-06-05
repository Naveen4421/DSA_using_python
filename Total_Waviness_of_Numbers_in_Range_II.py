#from functools import lru_cache
class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        #from functools import lru_cache
        def solve(x):
            if x < 0:
                return 0

            s = str(x)
            memo = {}

            def dp(pos, tight, started, prev2, prev1):
                key = (pos, tight, started, prev2, prev1)

                if key in memo:
                    return memo[key]

                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_count = 0
                total_wave = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, ntight, False, -1, -1)
                    else:
                        add = 0

                        if prev2 != -1:
                            if ((prev1 > prev2 and prev1 > d) or
                                (prev1 < prev2 and prev1 < d)):
                                add = 1

                        nprev2 = prev1 if prev1 != -1 else d
                        nprev1 = d

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            nprev2,
                            nprev1
                        )

                        wav += add * cnt

                    total_count += cnt
                    total_wave += wav

                memo[key] = (total_count, total_wave)
                return memo[key]

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)

        
