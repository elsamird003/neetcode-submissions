class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 1. Initialize the result array
        res = [1] * len(nums)

        # --- Pass 1: Calculate Prefix Products ---
        # Stores the product of all elements to the LEFT of index i
        prefix = 1
        for i in range(len(nums)):
            # Store the current prefix product (product up to nums[i-1])
            res[i] = prefix
            
            # Update the prefix for the next iteration (i+1)
            prefix *= nums[i]
        
        # Example for nums = [1, 2, 3, 4]:
        # res is now [1, 1, 2, 6] (Left Products)

        # --- Pass 2: Calculate Postfix Products and Final Result ---
        # 🐛 FIX: Initialize postfix outside the first loop
        postfix = 1 
        
        for i in range(len(nums) - 1, -1, -1):
            # res[i] now holds: (Left Product) * (Right Product)
            res[i] *= postfix
            
            # Update the postfix product for the next iteration (i-1)
            postfix *= nums[i]
            
        # Example for nums = [1, 2, 3, 4]:
        # i=3: res[3] = 6 * 1 = 6. postfix = 1 * 4 = 4
        # i=2: res[2] = 2 * 4 = 8. postfix = 4 * 3 = 12
        # i=1: res[1] = 1 * 12 = 12. postfix = 12 * 2 = 24
        # i=0: res[0] = 1 * 24 = 24. postfix = 24 * 1 = 24
            
        return res