class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # My first thought
    
        ans = []
        
        for i in range(2 * len(nums)):
            if i < len(nums):
                ans.append(nums[i]) 
            else: 
                ans.append(nums[i - len(nums)]) 

        return ans

         