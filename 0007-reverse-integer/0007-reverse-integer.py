class Solution(object):
    def reverse(self, x):

        neg = False

        if x==0:
            return 0
        elif x < 0:
            x = (-x)
            neg = True

        myint = 0
        val = 0
        while(x != 0):
            myint = x%10
        
            val*=10
            val+=myint

            x = x/10
        
        if val>(2**31):
            return  0
        
        if(neg):
            return (-val)
        else : return val
        