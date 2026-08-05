class Solution(object):
    def pivotIndex(self, nums):
        if sum(nums[1:len(nums)])==0:
            return 0
        for i in range(0,len(nums)):
            if sum(nums[0:i])==sum(nums[i+1:len(nums)]):
                return i
        
        return -1
        