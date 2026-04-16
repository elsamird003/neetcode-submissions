class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # Sort the list in place
        for i in range(len(nums) - 1): # Iterate up to the second to last element
            if nums[i] == nums[i + 1]: # Compare adjacent elements
                return True
        return False # Return False only after checking the whole list