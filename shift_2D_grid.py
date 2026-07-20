class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total  # no need to shift more than a full cycle

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                flat_idx = i * n + j
                new_flat_idx = (flat_idx + k) % total
                new_i = new_flat_idx // n
                new_j = new_flat_idx % n
                result[new_i][new_j] = grid[i][j]

        return result
