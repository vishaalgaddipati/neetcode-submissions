class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {} # hash map where difference : index are key val

        for i, n in enumerate(nums):
            if n in differences.keys():
                return [differences[n], i] # guaranteed a pair so can return in loop
            
            differences[target - n] = i