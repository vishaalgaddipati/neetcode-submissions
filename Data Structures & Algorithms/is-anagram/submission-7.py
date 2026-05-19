class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use dicts / hash maps to track char count where key -> char and val -> count
        hashmapS = {}
        hashmapT = {}

        for char in s:
            hashmapS[char] = hashmapS.get(char, 0) + 1  # return value else 0 if DNE

        for char in t:
            hashmapT[char] = hashmapT.get(char, 0) + 1
            
        return hashmapS == hashmapT