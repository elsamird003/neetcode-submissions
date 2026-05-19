class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxarea = 0

        for i in range(n):
            height = heights[i]
            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1

            leftMost = i

            while leftMost >= 0 and heights[leftMost] >= height:

                leftMost -= 1

            rightMost -= 1
            leftMost += 1

            maxarea = max(maxarea,height * (rightMost - leftMost + 1))
        return maxarea
        