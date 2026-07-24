class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1_000        
            }

        for j, k in zip(s, s[1:]):
            if romans[j] < romans[k]:
                res -= romans[j]
            else:
                res += romans[j]

        return res + romans[s[-1]]
