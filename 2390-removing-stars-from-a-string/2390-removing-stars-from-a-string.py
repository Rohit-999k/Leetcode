class Solution(object):
    def removeStars(self, s):
        
        a = ""
        for i in s:
            if i=='*':
                a = a[:-1]
            else:
                a = a+i
        return a