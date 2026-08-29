class Solution(object):
    def addDigits(self, num):
        if num<10:
            return num
        s = 0
        while(num!=0 or s>9):
            s += num%10
            num//=10
            if num==0 and s>9:
                num = s
                s = 0
        
        return s
        