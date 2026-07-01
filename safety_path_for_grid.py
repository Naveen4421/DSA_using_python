def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        import heapq
        n = len(grid)
        
        
        safeness = [[-1] * n for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    safeness[i][j] = 0
                    q.append((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and safeness[nx][ny] == -1:
                    safeness[nx][ny] = safeness[x][y] + 1
                    q.append((nx, ny))
        
        
        if safeness[0][0] == 0 or safeness[n-1][n-1] == 0:
            return 0
        
       
        visited = [[False] * n for _ in range(n)]
        max_heap = [(-safeness[0][0], 0, 0)]
        
        while max_heap:
            neg_val, x, y = heapq.heappop(max_heap)
            val = -neg_val
            
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            if x == n - 1 and y == n - 1:
                return val
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    
                    new_val = min(val, safeness[nx][ny])
                    heapq.heappush(max_heap, (-new_val, nx, ny))
        
        return 0
