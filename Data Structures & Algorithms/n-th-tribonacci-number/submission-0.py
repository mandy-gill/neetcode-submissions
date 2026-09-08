class Solution:
    def tribonacci(self, n: int) -> int:
        base = [0, 1, 1]

        if n <= 2:
            return base[n]

        for i in range(n - 2):
            base = [base[1], base[2], sum(base)]
        
        return base[2]
