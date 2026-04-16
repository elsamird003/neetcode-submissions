class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # This counts every letter in O(n) time
        return Counter(s) == Counter(t)  