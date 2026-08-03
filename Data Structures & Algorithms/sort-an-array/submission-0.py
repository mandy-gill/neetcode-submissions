class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return self.recursiveSort(nums)

    def recursiveSort(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums
        
        mid = math.floor(len(nums) / 2)
        a1 = self.recursiveSort(nums[:mid])
        a2 = self.recursiveSort(nums[mid:])
        return self.merge(a1, a2)

    def merge(self, a1: List[int], a2: List[int]) -> List[int]:
        a3 = []
        i, j = 0, 0

        while i < len(a1) and j < len(a2):
            if a1[i] <= a2[j]:
                a3.append(a1[i])
                i += 1

            elif a1[i] > a2[j]:
                a3.append(a2[j])
                j += 1

        if i != len(a1):
            while i != len(a1):
                a3.append(a1[i])
                i += 1
        
        if j != len(a2):
            while j != len(a2):
                a3.append(a2[j])
                j += 1

        return a3
            