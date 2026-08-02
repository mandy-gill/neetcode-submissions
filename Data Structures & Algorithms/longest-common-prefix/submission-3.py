class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # My first thought 

        lcp = strs[0]

        for s in strs:
            if s == "": 
                return ""

            for i, c in enumerate(s):
                if i < len(lcp):
                    if i == len(s) - 1:
                        lcp = lcp[0:i+1]
                        
                    if lcp[i] != c:
                        lcp = lcp[0:i]
                        break
                    

        return lcp