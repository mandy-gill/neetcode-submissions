class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0 # no. of elements not equal to val
        for n in nums:
            if n != val:
                k += 1

        someC = 0
        indices = []

        for i, n in enumerate(nums):
            
            if n != val:
                if len(indices) > 0:
                    nums[i] = nums[indices[0]]
                    nums[indices[0]] = n
                    indices.pop(0)
                    indices.append(i)
                someC += 1
                
            else:
                indices.append(i)

            if someC >= k:
                break

        return k