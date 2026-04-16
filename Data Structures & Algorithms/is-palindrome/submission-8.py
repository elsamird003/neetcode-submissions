class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Initialize the new string inside the method
        srt = ''
        
        # 2. Correctly indent the loop and its contents
        for c in s:
            # 3. Correct the typo from isalumn() to isalnum()
            if c.isalnum():
                srt += c.lower()
                
        # The logic to check if srt is a palindrome is correct
        return srt == srt[::-1]