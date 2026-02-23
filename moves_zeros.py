def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index=0  #index value to store the array value
        for i in range(len(nums)):
            if nums[i]!=0: # checking the non decimal value
                nums[index]=nums[i]   # adding using index value to same array
                index+=1  #incrementing index value
        for i in range(index,len(nums)):
            nums[i]=0  #adding remaining zeros to end of the array
        return nums
