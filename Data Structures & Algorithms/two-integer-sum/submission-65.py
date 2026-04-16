class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        
        for i, j in enumerate(nums):
            needed_num = target - j
            
            # This IF statement must be indented to stay INSIDE the loop
            if needed_num in has:
                return [has[needed_num], i]
            
            # This must be indented to stay INSIDE the loop, 
            # but OUTSIDE the IF statement
            has[j] = i
            
        return []