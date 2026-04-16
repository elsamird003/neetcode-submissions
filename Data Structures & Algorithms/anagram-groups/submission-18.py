class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Create a dictionary to store groups
        # Key: The sorted string, Value: List of anagrams
        anagram_map = {}
        
        for word in strs:
            # Sort the characters in the word to create a unique key
            # "eat" becomes "aet", "tea" becomes "aet"
            sorted_word = "".join(sorted(word))
            
            # If the key exists, add the word to that list
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            # If the key doesn't exist, create a new list
            else:
                anagram_map[sorted_word] = [word]
        
        # Return only the values (the groups) from the dictionary
        return list(anagram_map.values())