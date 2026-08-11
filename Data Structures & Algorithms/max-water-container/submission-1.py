class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        best = 0

        while i < j:
            y = min(heights[i], heights[j])
            x = j - i
            area = y * x
            best = max(best, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return best