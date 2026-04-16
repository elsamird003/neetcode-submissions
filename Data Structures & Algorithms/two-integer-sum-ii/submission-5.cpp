class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1; 

        while (left < right) {
            int sum = numbers[left] + numbers[right];

            if (sum == target) {
                // Return indices + 1 because the problem is "1-indexed"
                return {left + 1, right + 1}; 
            }
            else if (sum < target) {
                left++; // Too small, move left up
            }
            else {
                right--; // Too big, move right down
            }
        }
        
        // Since the problem says there is ALWAYS one solution, 
        // this line technically won't be reached, but C++ requires it.
        return {};
    }
};