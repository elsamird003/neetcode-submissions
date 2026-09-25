#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Map to store the number and its original index: <number, index>
        unordered_map<int, int> numMap; 
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i]; 
            
            // If the complement exists in our map, we found the pair
            if (numMap.count(complement)) {
                return {numMap[complement], i}; 
            }
            
            // Otherwise, add the current number and its index to the map
            numMap[nums[i]] = i; 
        }
        
        return {};
    }
};