class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "*", "-", "/"]

        for token in tokens:
            if token in ops:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "+":
                    stack.append(a + b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "-":
                    stack.append(b - a)
                else:
                    stack.append(b / a)
            else:
                stack.append(token)

        return int(stack.pop())