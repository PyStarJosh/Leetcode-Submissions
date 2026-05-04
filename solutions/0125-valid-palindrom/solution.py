import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        front = 0
        back = len(s) - 1

        while front < back:
            if s[front] != s[back]:
                return False
            front += 1
            back -= 1
            
        return True
