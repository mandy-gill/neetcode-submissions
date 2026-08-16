class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        index = 0

        for op in operations:
            print(scores)
            if self.isNumeric(op):
                scores.append(int(op))
                index += 1
            elif op == "+":
                scores.append(scores[index - 1] + scores[index - 2])
                index += 1
            elif op == "D":
                scores.append(2 * scores[index - 1])
                index += 1
            else:
                scores.pop()
                index -= 1

        res = 0
        for s in scores:
            res += s

        return res

    def isNumeric(self, s):
        for i, c in enumerate(s):
            if i == 0:
                if ord(c) != 45 and (ord(c) < 48 or ord(c) > 57):
                    return False
            else:
                if ord(c) < 48 or ord(c) > 57:
                    return False
        
        return True

                    