class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {} # storing counts of number, num : count
        
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)

        countArray = defaultdict(list) # count array, index is count and inside is array of all nums with that count
        for num, count in hashMap.items():
            countArray[count].append(num)
            # appending nums to array/list in bucket with corresponding count

        returnList = []
        count = 0
        for i in range(len(nums), 0, -1):
            for j in range(len(countArray[i])):
                returnList.append(countArray[i][j])
                count += 1
                if count == k:
                    return returnList


