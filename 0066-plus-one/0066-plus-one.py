class Solution(object):
    def plusOne(self, digits):
        s=""
        for i in range(0,len(digits)):
            s+= str(digits[i])

        val = int(s)
        val+=1
        s = str(val)

        l = []
        for i in range(0,len(s)):
             l.append(int(s[i]))
        return l
            
        