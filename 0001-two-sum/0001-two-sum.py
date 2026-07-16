class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        v = {}

        for i, num in enumerate(nums):
            if target - num in v:
                return [i, v[target - num]]
            v[num] = i
