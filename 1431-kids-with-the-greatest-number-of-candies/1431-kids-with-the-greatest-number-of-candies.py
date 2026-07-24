class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ls = []
        maximum_candy = max(candies)
        for i in range(0,len(candies)):
            if (candies[i]+extraCandies) >= maximum_candy:
                ls.append(True)
            else:
                ls.append(False)
        return ls