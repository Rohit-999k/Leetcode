class Solution(object):
    def isSubsequence(self, s, t):
        j=0
        count=0

        for i in s:

            if j>=len(t):
                return False

            while j<len(t):
                if t[j]==i:
                    j+=1
                    count+=1
                    break
                j+=1
            
            
        
        return len(s)==count