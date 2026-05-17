class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams (Ex: 1e, 1a, 1t : [eat, ate, ...])

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1 # using ASCII values to compute indices so a - a is 0

            res[tuple(count)].append(s) # lists can't be keys in python so use a tuple

        return res.values() # don't need keys anymore just anagram values