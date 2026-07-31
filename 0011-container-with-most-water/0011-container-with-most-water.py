class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        m = 0
        while l<r:
            a = min(height[l],height[r])
            if a*(r-l)>m:
                m = a*(r-l)
            
            if height[l]>height[r]:
                r=r-1
            else:
                l = l+1

        return m
        