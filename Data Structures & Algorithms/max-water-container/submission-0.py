class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max = 0
        while l < r:
            if heights[l] == heights[r]:
                currArea = heights[l] * (r - l)
                if currArea > max:
                    max = currArea
                l += 1
                r -= 1
            elif heights[l] < heights[r]:
                currArea = min(heights[l], heights[r]) * (r - l)
                if currArea > max:
                    max = currArea
                l += 1
            else:
                currArea = min(heights[l], heights[r]) * (r - l)
                if currArea > max:
                    max = currArea
                r -= 1
        return max