class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''.join(f'{len(s)}%{s}' for s in strs)
        return res

    def decode(self, s: str) -> List[str]:
        res, start_idx = [], 0

        while start_idx < len(s):
            char_idx = start_idx
            while s[char_idx] != '%':
                char_idx += 1
            length = int(s[start_idx:char_idx])
            res.append(s[char_idx + 1 : char_idx + 1 + length])
            start_idx = char_idx + 1 + length
        
        return res
