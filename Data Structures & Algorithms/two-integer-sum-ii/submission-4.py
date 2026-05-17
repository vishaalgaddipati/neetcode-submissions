class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use the idea that it is sorted and a left and right pointer to find a pair of solutions
        l, r = 0, len(numbers) - 1
        while (numbers[l] + numbers[r] != target):
            # if the sum of l and r is over target we decrement the right pointer
            if numbers[l] + numbers[r] > target:
                r -= 1
            # if the sum of l and r is less than target we increment the left ptr
            if numbers[l] + numbers[r] < target:
                l += 1
        return [l + 1, r + 1]
