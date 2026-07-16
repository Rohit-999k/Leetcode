class Solution(object):
    def twoSum(self, numbers, target):
        ls = []
        
        for i in range(0,len(numbers)-1):
            if (numbers[i]==numbers[i+1]) and (numbers[i]*2 != target):
                continue
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    ls.append(i+1)
                    ls.append(j+1)
                    return ls

        