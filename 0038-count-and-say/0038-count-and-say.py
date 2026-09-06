class Solution(object):
    def countAndSay(self, n):
        s = "1"

        for _ in range(1 , n):
            sol = []
            count =1

            for j in range(1 , len(s)):

                if s[j]==s[j-1]:
                    count += 1
                    
                else:
                    sol.append(str(count))
                    sol.append(s[j-1])
                    count = 1

            sol.append(str(count))
            sol.append(s[-1])

            s = "".join(sol)

        return s

