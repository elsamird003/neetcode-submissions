class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty = set()
        for i in nums:
            if i not in empty:
               empty.add(i)
            else: 
                return True
        return False