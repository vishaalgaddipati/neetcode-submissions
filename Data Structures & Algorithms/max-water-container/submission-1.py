class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left pointer at left and right at right to maximize width
        # then update l, r ptrs based on which is smaller, to maximize height
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res