class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums) {
        let result = 0;
        for (let i = 0; i < nums.length; i++) {
            result ^= nums[i]; // XOR each element with result
        }
        return result; // The single number remains
    }
}
