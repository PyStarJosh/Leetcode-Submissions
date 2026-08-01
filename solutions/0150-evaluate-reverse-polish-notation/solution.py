class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"*", "+" ,"-", "/"}

        for token in tokens:
            if token in operands:
                popped_val = stack.pop()

                match token:
                    case "*":
                        stack[-1] *= popped_val
                    case "+":
                        stack[-1] += popped_val
                    case "-":
                        stack[-1] -= popped_val
                    case "/": 
                        stack[-1] = int(stack[-1] / popped_val)
            else:
                stack.append(int(token))
        
        return stack[0]
