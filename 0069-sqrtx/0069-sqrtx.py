class Solution(object):
    def mySqrt(self, x):
        i = 0
        while i**2 <= x:
            i = i + 1

        return i - 1
        