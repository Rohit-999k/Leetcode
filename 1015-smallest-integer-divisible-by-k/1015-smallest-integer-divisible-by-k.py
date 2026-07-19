class Solution(object):
    def smallestRepunitDivByK(self, k):
        
        if(k%2==0 or k%5==0  ):
            return -1

        i=1
        for _ in range(0,100000):
            if i%k==0:
                return len(str(i))

            i = i*10+1
            
        return -1