class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = [ i for i in range(1, n + 1)]
        trustees = []

        for i, j in trust:
            if i in judge:
                judge.remove(i)

        if len(judge) == 1:
            for i, j in trust:
                if j == judge[0] and i not in trustees:
                    trustees.append(i)
            if len(trustees) == n - 1:
                return judge[0]

        return -1