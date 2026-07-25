class Solution(object):
    def reverseVowels(self, s):
        v = "aeiouAEIOU"
        a = ""
        final =""

        for i in s:
            if i in v:
                a = a + i

        a = a[::-1]

        j=0
        for i in range(0,len(s)):
            if s[i] in a:
                final = final+a[j]
                j+=1
            else:
                final = final + s[i]
        return final
                

        