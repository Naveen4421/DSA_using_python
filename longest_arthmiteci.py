class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        s=arr
        t=difference
        if not s:
            return 0
        d={}        #{1:1,5:1,7:1,8:1,5:2,3:3,4:1,2:2,1:4}
        max_value=0
        for ch in s:
            r=ch-(t)       #  1.1-(-2)=3  2.5-(-2)=7   3.7-(-2)=9 
            if r in d:     # we are checking the resulted after calculation 
                v=d[r]     # if that found then we need to get the value part in that like 
                d[ch]=v+1   # if we get the remainin value we are incrementing value 
            else:          # if not found with matching value 
                d[ch]=1    # then we are adding to dict with key and values 
            max_value=max(max_value,d[ch])    # for every iteration we are changing max value to get the max substring 
        return max_value  
        
