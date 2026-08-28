class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        minLen = 0

        for r in range(len(nums)):
            s += nums[r]

            while s >= target:
                minLen = min(minLen, r - l + 1) if minLen > 0 else (r - l + 1)
                s -= nums[l]
                l += 1

        return minLen