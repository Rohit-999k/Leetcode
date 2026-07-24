class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ls = []
        temp=0
        maximum_candy = max(candies)
        for i in range(0,len(candies)):
            temp=candies[i]+extraCandies
            if temp>=maximum_candy:
                ls.append(True)
            else:
                ls.append(False)
        return ls