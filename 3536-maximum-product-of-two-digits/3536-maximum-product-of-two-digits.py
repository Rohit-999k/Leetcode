class Solution(object):
    def maxProduct(self, n):
        a = n%10
        n=n/10
        b = n%10
        n=n/10

        if n==0:
            return a*b

        if b>a:
            temp = a
            a = b 
            b = temp

        while(n!=0):
            temp=n%10
            n=n/10

            if temp>a:
                b = a
                a = temp
            
            elif temp>b:
                b = temp
            
        return a*b
        