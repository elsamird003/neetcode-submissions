#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 1. Create the hash map
        // Key = sorted string, Value = list of original anagrams
        unordered_map<string, vector<string>> map;
        
        // 2. Group the anagrams
        for (string s : strs) {
            string key = s;
            sort(key.begin(), key.end()); // Sort the word to create the key (e.g., "cat" -> "act")
            
            // Attach the original word to the correct inner list in the map
            map[key].push_back(s);
        }
        
        // 3. Create the final list of lists
        vector<vector<string>> result;
        
        // 4. Move the grouped lists from the map into the final result
        for (auto pair : map) {
            // pair.second is the vector<string> (the value in the map)
            result.push_back(pair.second); 
        }
        
        return result;
    }
};