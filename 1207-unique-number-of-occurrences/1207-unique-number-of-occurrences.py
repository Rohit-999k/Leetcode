class Solution(object):
    def uniqueOccurrences(self, arr):
        a = set(arr)
        b = set()
        temp=0

        for x in a:
            temp = arr.count(x)
            if temp in b:
                return False
            else:
                b.add(temp)
        
        return True

        