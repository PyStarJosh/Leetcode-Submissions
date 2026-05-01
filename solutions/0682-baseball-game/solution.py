class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op == 'C':
                scores.pop()
            
            elif op == '+':
                result = scores[-1] + scores[-2]
                scores.append(result)
            
            elif op == 'D':
                result = scores[-1] * 2
                scores.append(result)
            
            else:
                scores.append(int(op))

        return sum(scores)
