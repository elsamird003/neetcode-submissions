class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dt = {}
        for i in nums:
            if i in dt:
                return True

            dt[i] = True
                
       
        return False
