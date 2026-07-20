class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)==1 or nums[0]>nums[1]:
            return 0
        elif nums[-1]>nums[-2]:
            return len(nums)-1
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i

        