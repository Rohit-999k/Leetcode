class Solution(object):
    def smallestNumber(self, n, t):
        p = 1
        for i in str(n):
            p *= int(i)

        while p % t!=0:
            n = n+1
            p = 1

            for i in str(n):
                p *= int(i)

        
        return n
        