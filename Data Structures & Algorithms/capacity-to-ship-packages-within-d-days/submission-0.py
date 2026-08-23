class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            k = (l + r) // 2
            d = 0
            s = 0

            for w in weights:
                if s + w <= k:
                    s += w
                else:
                    s = w
                    d += 1
            d += 1   

            if d <= days:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
            
    