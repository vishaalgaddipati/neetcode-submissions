class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # i is the index and a is the value
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # [-2(l), -2, 0, 0, 2, 2(r)] we want to update left but avoid dupe like -2 so need to get to 0, same will happen for right, so only need to update 1 ptr
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res