class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        # Sort by values in descending order so O(nlogn)
        sortedDict = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))

        res = list(sortedDict.keys())
        return res[:k]
            