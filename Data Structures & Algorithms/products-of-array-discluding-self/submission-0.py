class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums) + 1)]
        suffix = [1 for _ in range(len(nums) + 1)]

        for i in range(0, len(nums), 1):
            prefix[i + 1] = prefix[i] * nums[i]
        
        for i in range(len(nums)-1, 0, -1):
            suffix[i - 1] = suffix[i] * nums[i]

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])

        return output
        