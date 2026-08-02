class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # My first thought
        
        if len(s) != len(t):
            return False

        hashmapS = {}
        hashmapT = {}

        for i in range(len(s)):
            hashmapS[s[i]] = hashmapS.get(s[i], 0) + 1
            hashmapT[t[i]] = hashmapT.get(t[i], 0) + 1

        chars = hashmapS.keys()

        for c in chars:
            if c not in hashmapT.keys() or hashmapS[c] != hashmapT[c]:
                return False
        
        return True
            