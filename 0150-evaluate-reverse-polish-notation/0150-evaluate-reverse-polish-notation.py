class Solution:
    def isExpression(self, token: str) -> bool:
        return (token in "+-*/")
    
    def evalEquation(self, x: int, y: int, operand: str) -> int:
        match operand:
            case "+":
                return x + y
            case "-":
                return x - y
            case "*":
                return x * y
            case "/":
                return math.trunc(x / y)
            case _:
                raise f"No valid operand found for {operand} in {a} {operand} {b}."

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if (self.isExpression(token)):
                y, x = stack.pop(), stack.pop()
                stack.append(self.evalEquation(x, y, token))
            else:
                stack.append(int(token))
        
        return stack[0]




        