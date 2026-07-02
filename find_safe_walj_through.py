def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        from collections import deque
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        dq = deque([(0, 0)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while dq:
            r, c = dq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]  # 0 or 1
                    nd = dist[r][c] + cost
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        if cost == 0:
                            dq.appendleft((nr, nc))  # free move, explore first
                        else:
                            dq.append((nr, nc))       # costly move, explore later

        return health - dist[m - 1][n - 1] > 0
