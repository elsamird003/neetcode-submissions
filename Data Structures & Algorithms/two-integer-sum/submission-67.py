class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i,j in enumerate(nums):
            needed_sum = target - j
            if needed_sum in has:
                return [has[needed_sum],i]

            has[j] = i  ## J is the number itself and we need to add it to the index, if we the number is not in the dictionary or hash map
        return []