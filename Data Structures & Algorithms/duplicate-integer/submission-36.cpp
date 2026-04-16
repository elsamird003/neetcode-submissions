#include<unordered_set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std:unordered_set<int> seen;
        for (int j : nums){
            if(seen.find(j) !=  seen.end()){
                return true;
            }
            seen.insert(j);

 
        }
                return false;
    }
};