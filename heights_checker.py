def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s=sorted(heights)
        n=len(heights)
        count=0
        for i in range(n):
            if(heights[i]!=s[i]):
                count+=1
            else:
                continue
        return count
