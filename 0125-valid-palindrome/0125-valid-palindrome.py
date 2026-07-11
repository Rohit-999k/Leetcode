class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = ""

        for i in s:
            if i.isalnum():
               v += i.lower()
        return v == v[ : :-1]