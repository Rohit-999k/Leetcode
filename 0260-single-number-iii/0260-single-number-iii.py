class Solution(object):
    def singleNumber(self, nums):
        if len(nums)==2:
            return nums
        total = 0
        for i in nums:
            total ^= i

        dif = (total & -total)

        a = 0
        b = 0
        for i in nums:
            if i & dif:
                a ^= i
            else:
                b ^= i

        return [a, b]