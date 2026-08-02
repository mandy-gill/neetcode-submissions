class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use a simple hash set to keep track of previously seen elements
        
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False