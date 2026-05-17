class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnList = []
        visited = [False] * len(strs) # track visited strings

        for i in range(len(strs)):
            if visited[i]:
                continue

            countS = {}
            countComp = {}
            currString = strs[i]
            currSublist = [currString]
            for j in range(len(currString)):
                countS[currString[j]] = 1 + countS.get(currString[j], 0)
            for j in range(i + 1, len(strs)):
                if visited[j]:
                    continue

                compareString = strs[j]
                for k in range(len(compareString)):
                    countComp[compareString[k]] = 1 + countComp.get(compareString[k], 0)
                if countS == countComp:
                    currSublist.append(compareString)
                    visited[j] = True
                countComp = {} # resetting count comp for next word
            returnList.append(currSublist)
            visited[i] = True
        return returnList