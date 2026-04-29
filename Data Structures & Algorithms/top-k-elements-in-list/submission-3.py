from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        top_elements = counter.most_common(k)

        new_L = []
        for i, freq in top_elements:
            new_L.append(i)
            
        return new_L