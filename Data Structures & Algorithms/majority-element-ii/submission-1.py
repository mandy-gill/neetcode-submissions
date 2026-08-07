class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        majority = []
        for c in count:
            if count[c] > (len(nums) // 3):
                majority.append(c)

        return majority