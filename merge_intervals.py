def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        merged=[intervals[0]]
        for start,end in intervals[1:]:
            last=merged[-1]
            if start<=last[1]:
                last[1]=max(last[1],end)
            else:
                merged.append([start,end])
        return merged
