class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        store = set(nums)  # Step 1: O(n) to create the set
        
        for n in store:
            # Step 2: Check if 'n' is the start of a sequence
            # If n-1 is NOT in the set, then 'n' is the starting number.
            if (n - 1) not in store:
                # 'n' is the start, begin counting
                current_length = 1
                current_num = n
                
                # Step 3: Check for the next consecutive numbers
                # Keep going as long as the next number is in the set
                while (current_num + 1) in store:
                    current_num += 1
                    current_length += 1
                
                # Step 4: Update the maximum length found so far
                res = max(res, current_length)
                
        return res