class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        
        while (left <= right) {
            // Find the middle index
            // (left + right) / 2 works, but this prevents integer overflow
            int mid = left + (right - left) / 2; 
            
            if (nums[mid] == target) {
                return mid; // Found it!
            }
            
            if (nums[mid] < target) {
                // Target must be in the right half, so move the left pointer
                left = mid + 1;
            } else {
                // Target must be in the left half, so move the right pointer
                right = mid - 1;
            }
        }
        
        // If the loop finishes, the target wasn't in the array
        return -1; 
    }
};