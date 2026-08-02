class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Variable # of concetanations
        # O(2n) = O(n)

        numConcat = 2
        ans = []

        for i in range(numConcat):
            for n in nums:
                ans.append(n)

        return ans