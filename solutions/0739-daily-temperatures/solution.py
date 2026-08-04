class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0] * n
        temp_stack = []

        for idx in range(n):

            while temp_stack and temps[temp_stack[-1]] < temps[idx]:
                top_idx = temp_stack.pop()
                res[top_idx] = idx - top_idx
            
            temp_stack.append(idx)

        return res
