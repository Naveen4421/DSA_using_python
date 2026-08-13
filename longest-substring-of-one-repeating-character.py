class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        s = list(s)

        # Segment tree arrays (1-indexed, size 4*n)
        size = [0] * (4 * n)
        lc = [""] * (4 * n)
        rc = [""] * (4 * n)
        lrun = [0] * (4 * n)
        rrun = [0] * (4 * n)
        mx = [0] * (4 * n)

        def pushup(u):
            left, right = u * 2, u * 2 + 1
            size[u] = size[left] + size[right]

            lc[u] = lc[left]
            rc[u] = rc[right]

            lrun[u] = lrun[left]
            if lrun[left] == size[left] and rc[left] == lc[right]:
                lrun[u] += lrun[right]

            rrun[u] = rrun[right]
            if rrun[right] == size[right] and lc[right] == rc[left]:
                rrun[u] += rrun[left]

            mx[u] = max(mx[left], mx[right])
            if rc[left] == lc[right]:
                mx[u] = max(mx[u], rrun[left] + lrun[right])

        def build(u, l, r):
            if l == r:
                size[u] = 1
                lc[u] = rc[u] = s[l]
                lrun[u] = rrun[u] = mx[u] = 1
                return
            mid = (l + r) // 2
            build(u * 2, l, mid)
            build(u * 2 + 1, mid + 1, r)
            pushup(u)

        def update(u, l, r, idx, ch):
            if l == r:
                lc[u] = rc[u] = ch
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(u * 2, l, mid, idx, ch)
            else:
                update(u * 2 + 1, mid + 1, r, idx, ch)
            pushup(u)

        build(1, 0, n - 1)

        result = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            result.append(mx[1])

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestRepeating("babacc", "bcb", [1, 3, 3]))  # [3, 3, 4]
    print(sol.longestRepeating("abyzz", "aa", [2, 1]))        # [2, 3]
