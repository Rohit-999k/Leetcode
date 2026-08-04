class Solution(object):
    def findMissingElements(self, nums):
        ls = []
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                ls.append(i)
            
        return ls
        