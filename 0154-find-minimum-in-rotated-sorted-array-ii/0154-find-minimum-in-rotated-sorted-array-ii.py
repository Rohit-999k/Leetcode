class Solution(object):
    def findMin(self, nums):
       min = nums[0]
       for i in range(1,len(nums)):
            j=-i
            if nums[i]<min:
                min=nums[i]
            elif nums[j]<min:
                min=nums[j]
            
            if i>len(nums)/2:
                break
        
       return min

        