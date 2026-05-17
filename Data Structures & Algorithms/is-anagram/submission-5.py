class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myMap1 = {}
        myMap2 = {}

        # Use a dict/hash map to store letter as key and count as value, then compare dicts
        for char in s:
            myMap1[char] = myMap1.get(char, 0) + 1

        for char in t:
            myMap2[char] = myMap2.get(char, 0) + 1

        return myMap1 == myMap2
 