class Solution:
    def reverseString(self, s: List[str]) -> None:
        front, back = 0, len(s) - 1

        while front < back:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1
            
        """
        Do not return anything, modify s in-place instead.
        """
