class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        # Sort the hashmap by values in reverse order and get the top k keys
        sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        
        # Extract just the keys for the top k frequent elements
        return [item[0] for item in sorted_items[:k]]
