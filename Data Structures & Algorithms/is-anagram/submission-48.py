class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Quick check: If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False

        # 2. Setup our two hash maps
        countS, countT = {}, {}

        # 3. Populate both hash maps at the same time
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)  # Fixed the 'countT' typo here!

        # 4. If the dictionaries are identical, it's an anagram!
        return countS == countT