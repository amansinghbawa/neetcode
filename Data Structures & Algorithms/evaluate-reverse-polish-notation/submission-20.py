
ops = ["+", "-", "*", "/"]

class Solution:
    
    @staticmethod
    def solve_postfix(tokens):
        """
        1+2         12+ 
        1-2*3       123*-
        (1-2)*3     12-3*
        """
        operands = []
        # operands = []
        if len(tokens) == 1:
            return int(tokens.pop())
        for token in tokens:
            if token in ops:
                first = operands.pop()
                second = operands.pop()
                if token == "+":
                    result = second + first
                elif token == "-":
                    result = second - first
                elif token == "*":
                    result = second * first
                else:
                    result = int(second / first)

                operands.append(result)
            else:
                operands.append(int(token))
        return operands.pop()


    def evalRPN(self, tokens: List[str]) -> int:
        return self.solve_postfix(tokens)
