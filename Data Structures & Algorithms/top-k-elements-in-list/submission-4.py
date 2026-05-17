class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map: num -> count
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # array where index is count and value is array of nums w/ that count
        buckets = [[] for i in range(len(nums) + 1)] # + 1 since we want the top index to be the max size
        for key, value in count.items():
            buckets[value].append(key)

        # now reverse iterate over buckets and get vals w/ k highest counts
        result = []
        # or could do len(buckets) - 1 since that equals len(nums)
        for i in range(len(nums), 0, -1): # O(n) + O(n) explained in video so not squared
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result