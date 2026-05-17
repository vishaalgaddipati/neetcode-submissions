class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # need to sort, then run two sum
        nums.sort()
        result = []

        for i in range(len(nums)):
            a = i
            # skip duplicates
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            
            # if we reach positive numbers, we know sum can never be zero since it's sorted
            if nums[a] > 0:
                break
            
            # left and right pointer
            b, c = i + 1, len(nums) - 1

            while b < c:
                curSum = nums[a] + nums[b] + nums[c]
                if (curSum == 0):
                    result.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    # skip duplicates
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
                elif (curSum > 0):
                    c -= 1
                elif (curSum < 0):
                    b += 1

        return result