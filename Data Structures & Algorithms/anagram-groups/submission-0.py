class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMaps = []
        res = []

        for s in strs:
            count = {}
            for c in s:
                count[c] = 1 + count.get(c, 0)
            
            if count in prevMaps:
                index = prevMaps.index(count)
                res[index].append(s)
            else:
                prevMaps.append(count)
                res.append([s])
        
        return res