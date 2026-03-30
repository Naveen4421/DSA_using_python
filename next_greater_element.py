def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in nums1:
            found=False
            for j in range(len(nums2)):
                if(i==nums2[j]):
                    for k in range(j+1,len(nums2)):
                        if(i<nums2[k]):
                            result.append(nums2[k])
                            found=True
                            break
            if not found:
                result.append(-1)
        return result
