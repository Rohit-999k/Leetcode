class Solution(object):
    def findDuplicate(self, nums):
        ls = set()
        for i in nums:
            if i not in ls:
                ls.add(i)
            else: return i
            
        