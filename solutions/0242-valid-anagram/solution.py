from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = defaultdict(int)

        for index in range(len(s)):
            seen[s[index]] += 1

        for index in range(len(t)):
            if t[index] in seen:
                seen[t[index]] -= 1
        
        for val in seen.values():
            if val != 0:
                return False
        
        return True
