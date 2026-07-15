class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        r = ""
        for i in range(len(s)-1,-1,-1):
            r += s[i] + " "
        
        return r.strip()

        