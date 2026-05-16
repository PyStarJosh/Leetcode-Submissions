import re

class Solution:
    def validPalindrome(self, s: str) -> bool:        
        char1, char2 = self._helper_window_sliding(s)

        if char1 == -1 :
            return True

        else: 
            s2 = s[:char1] + s[char1 + 1:]
            s3 = s[:char2] + s[char2 + 1:]
            is_s2_palindrome = self._helper_window_sliding(s2)
            is_s3_palindrome = self._helper_window_sliding(s3)

            if (is_s2_palindrome[0] == -1) or (is_s3_palindrome[0] == -1):
                return True

            return False

    def _helper_window_sliding(self, s: str) -> tuple:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        front = 0
        back = len(s) - 1
    
        while front < back:
            if s[front] != s[back]:
                return front, back
            
            front += 1
            back -= 1

        return -1, -1

  '''This problem was a struggle for me, but I managed to construct this O(n) space and time complexity answer. You can tell it took a bit out of me because I named the helper window_sliding while using a 2-pointer algo. Nonetheless,
  I reassessed the problem and optimized my solution to achieve O(n) time and O(1) space complexity with succinct code.'''
