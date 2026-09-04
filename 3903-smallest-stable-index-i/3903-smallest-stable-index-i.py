class Solution(object):
    def firstStableIndex(self, nums, k):
        ls = []
        for i in range(len(nums)):
            ls.append(max(nums[:i+1])-min(nums[i:len(nums)]))

        for i in range(len(ls)):
            if ls[i]<=k:
                return i
        
        return -1
        