class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

        for index in range(len(s)):
            char = s[index]

            if char in brackets_dict.keys():
                stack.append(char)

            elif char in brackets_dict.values():
                if not stack:
                    return False
                else:
                    opening_brace = stack.pop()
            
                if brackets_dict[opening_brace] != char:
                    return False
        
        return len(stack) == 0
