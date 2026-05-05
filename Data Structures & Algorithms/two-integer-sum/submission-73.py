class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store: { number: index }
        seen = {}
        
        for i, num in enumerate(nums):
            # Calculate what number we need to reach the target
            complement = target - num
            
            # If we already saw that required number, we found our pair!
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, save the current number and its index in the dictionary
            seen[num] = i