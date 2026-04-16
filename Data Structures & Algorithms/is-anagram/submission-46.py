class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {} # DIctionary
        if len(s) != len(t): # basic bottleneck, base statement
            return False

        # Step 3: Count letters in 's' and subtract letters in 't' (O(N))
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1

        if all(val == 0 for val in count.values()):
            return True
        
        return False