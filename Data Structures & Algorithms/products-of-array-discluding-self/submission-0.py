class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # [1, 2, 4, 6] prefixes: [1, 1, 2, 8] suffixes: [48, 24, 6, 1]
        prefixProds, suffixProds = [1]*len(nums), [1]*len(nums)
        currPrefixProd, currSuffixProd = 1, 1
        for i in range(1, len(nums)):
            currPrefixProd *= nums[i-1]
            prefixProds[i] = currPrefixProd
        for i in range(len(nums) - 2, -1, -1):
            currSuffixProd *= nums[i+1]
            suffixProds[i] = currSuffixProd
        for i in range(len(nums)):
            res.append(prefixProds[i] * suffixProds[i])
        return res