class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max = 0

        while i < j:
            if heights[i] < heights[j]:
                y = heights[i]
            else:
                y = heights[j]
            x = j - i
            if y * x > max:
                max = y * x
            elif heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max
            
