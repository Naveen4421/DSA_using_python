class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        n = len(coins)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return (a * b) // gcd(a, b)
        
        def count_multiples(x):
            total = 0
            for mask in range(1, 1 << n):
                subset_lcm = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        subset_lcm = lcm(subset_lcm, coins[i])
                        bits += 1
                        if subset_lcm > x:
                            break
                if subset_lcm > x:
                    continue
                if bits % 2 == 1:
                    total += x // subset_lcm
                else:
                    total -= x // subset_lcm
            return total
        
        low = min(coins)
        high = min(coins) * k
        
        while low < high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low
