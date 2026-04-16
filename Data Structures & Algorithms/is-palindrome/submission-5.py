class Solution:
    def isPalindrome(self, s: str) -> bool:
        cp= ''
        for c in s:
            if c.isalnum():
                cp += c.lower()
        return cp == cp[::-1]
        