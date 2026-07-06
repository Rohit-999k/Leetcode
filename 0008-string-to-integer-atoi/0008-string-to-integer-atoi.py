class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        allowlist = ['0','1','2','3','4','5','6','7','8','9']
        first =0
        pos = True
        if s[0] == '-':
            first = 1
            pos = False
        elif (s[0]== '+'):
            first = 1
            pos = True

        val = 0

        for i in range(first,len(s)):
            if s[i] not in allowlist:
                break
            else :
                val*=10
                val+=int(s[i])

        if pos:
            if val>(2**31 -1):
                return (2**31 - 1)
            else: return val
        else : 
            if val> (2**31):
                return (-(2**31))
            else: return (-val)

       
        