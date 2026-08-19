# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        if guess(1) == 0:
            return 1
        elif guess(n) == 0:
            return n
        lb = 1
        ub = n
        while(lb<ub):
            mid = (lb+ub)//2
            value = guess(mid)

            if(value == 0):
                return mid
            elif(value == -1):
                ub = mid-1
            else:
                lb = mid+1
        return lb   
        
        