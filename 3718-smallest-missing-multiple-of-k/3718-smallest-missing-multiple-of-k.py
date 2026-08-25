class Solution(object):
    def missingMultiple(self, nums, k):
        for i in range(1,1001):
            if i*k not in nums:
                return i*k
        