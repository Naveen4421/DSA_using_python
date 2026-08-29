class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        value_index_pairs = sorted([(nums[i], i) for i in range(n)])
        
        
        components = []
        current_component = [value_index_pairs[0]]
        
        for i in range(1, n):
            
            if value_index_pairs[i][0] - value_index_pairs[i-1][0] <= limit:
                current_component.append(value_index_pairs[i])
            else:
                components.append(current_component)
                current_component = [value_index_pairs[i]]
        components.append(current_component)  
        
        
        ans = [0] * n
        for component in components:
            values = sorted([pair[0] for pair in component])
            indices = sorted([pair[1] for pair in component])
            for idx, val in zip(indices, values):
                ans[idx] = val
                
        return ans

        
