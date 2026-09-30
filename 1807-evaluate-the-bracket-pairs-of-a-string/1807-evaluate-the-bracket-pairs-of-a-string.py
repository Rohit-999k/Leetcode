class Solution(object):
    def evaluate(self, s, knowledge):
        ans = ""
        count = 0
        key = ""
        d = dict(knowledge)
        i=0

        while i< len(s):
            if s[i]!='(':
                ans += s[i]
            else:
                i+=1
                while(s[i]!=')'):
                    key+=s[i]
                    i+=1
                ans+= (d.get(key, "?"))
                key = ""
            
            i+=1

        return ans


        