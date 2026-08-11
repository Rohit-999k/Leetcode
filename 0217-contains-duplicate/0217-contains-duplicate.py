class Solution(object):
    def containsDuplicate(self, nums):
        x = set(nums)
        return len(x)!=len(nums)
        