import numpy as np

class Solution(object):
    def productExceptSelf(self, nums):
        if nums.count(0)==len(nums):
            return nums
        elif nums.count(0)>1:
            return list(np.zeros((len(nums),), dtype=np.int_))

        if 0 in nums:
            m = 1
            for i in nums:
                if i!=0:
                    m*=i
            
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=m
                else:
                    nums[i]=0
            
            return nums

        else:
            m = 1
            for i in nums:
                m*=i
            
            for i in range(len(nums)):
                nums[i]= m//nums[i]
            
            return nums


        