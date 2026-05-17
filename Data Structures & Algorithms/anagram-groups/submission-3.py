class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCounts = {}

        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            counts = tuple(counts)
            if counts not in charCounts:
                charCounts[counts] = []
            charCounts[counts].append(word)

        return charCounts.values()

        