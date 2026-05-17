class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if number before curr num not in set, then it must be start of new sequence and we count from there
        hashSet = set()
        for num in nums:
            hashSet.add(num)

        maxLength = 0
        for num in hashSet:
            # part of sequence
            if num-1 in hashSet:
                continue
            # start of a new sequence
            else:
                currLength = 1
                currNum = num
                while currNum+1 in hashSet:
                    currLength += 1
                    currNum += 1
                maxLength = max(maxLength, currLength)

        return maxLength