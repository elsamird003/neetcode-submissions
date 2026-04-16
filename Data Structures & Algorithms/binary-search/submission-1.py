class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Corrected mid calculation to avoid potential overflow
            mid = left + ((right - left) // 2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # Discard the right half
                right = mid - 1
            else:
                # Discard the left half
                left = mid + 1
                
        return -1