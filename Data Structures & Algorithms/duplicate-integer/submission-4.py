class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        # Iterate through nums and check if any duplicates
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        
        return False