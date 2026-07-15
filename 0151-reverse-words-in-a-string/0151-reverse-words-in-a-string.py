class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.strip().split()
        r = ""
        for i in range(len(k)-1,-1,-1):
            r += k[i] + " "
        
        return r.strip()

        