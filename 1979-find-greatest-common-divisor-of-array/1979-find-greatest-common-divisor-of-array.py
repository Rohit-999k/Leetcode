class Solution:
    def findGCD(self, nums: List[int]) -> int:
        l = min(nums)
        h = max(nums)
        for i in range(l,0,-1):
            if l%i==0 and h%i==0:
                return i
        