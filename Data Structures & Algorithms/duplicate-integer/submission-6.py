class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for j in range(len(nums)):
            for i in range(j + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True 
        return False 
        