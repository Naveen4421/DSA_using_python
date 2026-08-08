class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)

        # E[i]: min j such that word2[j:] is an exact subsequence of word1[i:]
        E = [0] * (n + 1)
        E[n] = m
        for i in range(n - 1, -1, -1):
            j = E[i + 1]
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
            E[i] = j

        # O[i]: min j such that word2[j:] embeds in word1[i:] with <=1 mismatch
        O = [0] * (n + 1)
        O[n] = m
        for i in range(n - 1, -1, -1):
            cand = [O[i + 1], E[i]]
            if E[i + 1] > 0:
                cand.append(E[i + 1] - 1)
            if O[i + 1] > 0 and word1[i] == word2[O[i + 1] - 1]:
                cand.append(O[i + 1] - 1)
            O[i] = min(cand)

        def can_finish(i, j, budget):
            return E[i] <= j if budget == 0 else O[i] <= j

        res = []
        p, budget = 0, 1
        for j in range(m):
            k = p
            found = -1
            mode = None
            while k < n:
                if word1[k] == word2[j]:
                    if can_finish(k + 1, j + 1, budget):
                        found, mode = k, 'exact'
                        break
                elif budget > 0 and can_finish(k + 1, j + 1, budget - 1):
                    found, mode = k, 'change'
                    break
                k += 1
            if found == -1:
                return []
            res.append(found)
            p = found + 1
            if mode == 'change':
                budget -= 1
        return res
        
