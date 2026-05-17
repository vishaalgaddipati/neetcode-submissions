class Solution:

    def encode(self, strs: List[str]) -> str:
        # follow scheme ["test", "abc"] -> "4#test3#abc"
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        currInd = 0
        res = []
        # remember length can be more than 1 char so 10 instead of 9
        while (currInd < len(s)):
            length = ""
            while (s[currInd] != "#"):
                length += s[currInd]
                currInd += 1
            length = int(length)
            chunk = ""
            for i in range(currInd + 1, currInd + length + 1):
                chunk += s[i]
            res.append(chunk)
            currInd = currInd + length + 1
        return res