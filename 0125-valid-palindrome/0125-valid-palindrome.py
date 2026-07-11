class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = "".join(char.lower() for char in s if char.isalnum())
        return v == v[ : :-1]