from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v, cost in edges:
            adj[u].append((v, cost))
            indeg[v] += 1

        topo = []
        q = deque(i for i in range(n) if indeg[i] == 0)
        indeg_copy = indeg[:]
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                indeg_copy[v] -= 1
                if indeg_copy[v] == 0:
                    q.append(v)

        def feasible(threshold):
            dp = [float('inf')] * n
            dp[0] = 0
            for u in topo:
                if dp[u] == float('inf') or not online[u]:
                    continue
                for v, cost in adj[u]:
                    if cost >= threshold and online[v]:
                        nd = dp[u] + cost
                        if nd < dp[v]:
                            dp[v] = nd
            return dp[n - 1] <= k

        costs = sorted(set(c for _, _, c in edges))
        lo, hi = 0, len(costs) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
