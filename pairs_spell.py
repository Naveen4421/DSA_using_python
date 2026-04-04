def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        from bisect import bisect_left

        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            # ceil(success / spell)
            target = (success + spell - 1) // spell
            
            idx = bisect_left(potions, target)
            result.append(n - idx)

        return result
