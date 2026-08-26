class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        
        checked = set()
        for i in s:
            if i in checked:
                continue
            checked.add(i)

            if s.count(i)!=t.count(i):
                return False
        
        return True
        