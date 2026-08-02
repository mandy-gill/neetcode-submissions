class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Append input array to itself and return it
        # O(n)
        
        for i in range(len(nums)):
            nums.append(nums[i])

        return nums