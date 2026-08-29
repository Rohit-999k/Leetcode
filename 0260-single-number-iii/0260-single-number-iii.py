class Solution(object):
    def singleNumber(self, nums):
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