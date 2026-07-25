class Solution(object):
    def reverseVowels(self, s):
        v = "aeiouAEIOU"
        left = 0
        right = len(s)-1
        final=""

        s = list(s)
        while(left<right):
            if str(s[left]) not in v:
                left+=1
                continue
            
            elif str(s[right]) not in v:
                right-=1
                continue
            
            else:
                s[left],s[right] = s[right] , s[left]
                left+=1
                right-=1
        
        for i in s:
            final = final + str(i)

        return final
            
        
        