class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        count=Counter(nums)
        return [num for num,freq in count.most_common(k)]


        


        
