class Solution(object):
    def isHappy(self, n):
        s = n
        ls = [n]
        while(s !=1):
            temp = s
            s = 0
            while(temp != 0):
                s += (temp%10)**2
                temp = temp//10
            
            if s in ls:
                return False
            else:
                ls.append(s)

        return True