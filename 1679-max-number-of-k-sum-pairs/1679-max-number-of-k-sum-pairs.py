class Solution(object):
    def maxOperations(self, numbers, target):
        numbers.sort()
        count =0
        lb,ub=0,len(numbers)-1
        while(lb<ub):
            if numbers[lb]+numbers[ub]==target:
                count+=1
                lb+=1
                ub-=1
            elif numbers[lb]+numbers[ub]<target:
                lb+=1
            else:
                ub-=1
        
        return count

        