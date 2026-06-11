class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict, deque
        MOD = 10**9 + 7

        n = len(edges) + 1

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to find maximum depth
        q = deque([(1, 0)])
        visited = {1}
        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, depth + 1))

        return pow(2, max_depth - 1, MOD)
        
