class Solution(object):
    def countAndSay(self, n):
        s = "1"
    
        for i in range(1,n):
            sol = ""
            prev = s[0]

            count =  0
            j = 0
            while(j<len(s)):
                if prev == s[j]:
                    count+=1
                else:
                    sol += (str(count)+prev)
                    count = 1
                    prev = s[j]
                
                j+=1
            
            sol += (str(count)+prev)

            s = sol
        
        return s


            

        