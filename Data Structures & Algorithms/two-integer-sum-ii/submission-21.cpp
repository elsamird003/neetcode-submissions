class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        // FIX 1: Set left to 0 and right to the last item
        int left = 0; 
        int right = numbers.size() - 1;
         
        while(left < right){
            int current_sum = numbers[left] + numbers[right];

            // FIX 2: Check for exact equality
            if (current_sum == target){
                return {left + 1, right + 1};
            }
            else if (current_sum < target){
                left++;
            }
            // FIX 3: Remove the condition from the final else
            else {
                right--;
            }
        }
        
        return {};
    }
};