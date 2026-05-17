class Solution:
    def trap(self, height: List[int]) -> int:
        # use maxL and maxR to track the max as we update L and R
        maxL, maxR = height[0], height[len(height) - 1]
        l, r = 0, len(height) - 1
        res = 0
        
        while (l < r):
            if (maxL <= maxR):
                l += 1
                trapped = maxL - height[l]
                if (trapped > 0):
                    res += trapped
                maxL = max(maxL, height[l])
            elif (maxL > maxR):
                r -= 1
                trapped = maxR - height[r]
                if (trapped > 0):
                    res += trapped
                maxR = max(height[r], maxR)
        return res

