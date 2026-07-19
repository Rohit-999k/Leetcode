class Solution(object):
    def selfDividingNumbers(self, left, right):
        ls =[]
        rem = 0
        copy = 0
        for i in range(left,right+1):
            if i%10==0:
                continue
            
            flag=0
            copy=i
            while(copy>0):
                rem = copy%10
                if copy%10==0:
                    flag=1
                    break
                if(i%rem == 0):
                    copy=copy/10
                    continue
                else:
                    flag=1
                    break
            if flag==0:
                ls.append(i)
        return ls

        