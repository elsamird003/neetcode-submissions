class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # the two strings better have both the same length
        return sorted(s) == sorted(t)
 

    
        