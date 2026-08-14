class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def swap(a, i, j):
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

        i = 0
        j = len(s) - 1

        while j >= i:
            swap(s, i, j)
            i += 1
            j -= 1