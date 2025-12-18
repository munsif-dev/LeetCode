class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        i = 2
        while i < len(tokens):
            if tokens[i] in ["*", "+", "-", "/"]:
                match tokens[i]:
                    case "+":
                        tokens[i-2:i+1] = [int(tokens[i-1]) + int(tokens[i-2])]
                    case "-":
                        tokens[i-2:i+1] = [int(tokens[i-2]) - int(tokens[i-1])]
                    case "*":
                        tokens[i-2:i+1] = [int(tokens[i-1]) * int(tokens[i-2])]
                    case "/":
                        tokens[i-2:i+1] = [int(tokens[i-2]) / int(tokens[i-1])]
                i = 2
            else:
                i += 1
        
        return int(tokens[0])
                
