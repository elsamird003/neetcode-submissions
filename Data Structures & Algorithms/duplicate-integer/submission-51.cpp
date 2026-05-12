#include <vector>
#include <set>

class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::set<int> mynumbers;

        // 1. You need a loop to check each number in the vector
        for (int n : nums) {
            // 2. Check if the current number 'n' is already in the set
            if (mynumbers.contains(n)) {
                return true; // Found a duplicate!
            }
            // 3. If not found, add this number to the set and keep looking
            mynumbers.insert(n);
        }

        // 4. If the loop finishes, no duplicates were found
        return false;
    }
};