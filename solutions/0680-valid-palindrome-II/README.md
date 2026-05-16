# 0680. Valid Palindrome II

**Difficulty:** Easy

**Topics:** Two Pointer

**Link:** https://leetcode.com/problems/valid-palindrome-ii/

## Approach
This problem asks you to return a boolean value stating the string given is a palindrome and you are allowed to remove at most one character. I initially knew I would utilize a 2-pointer algo to solve this problem that when I came across two values
that didnt match. I would check if the string was a palindrome without either one seperately, I decided to enlist the use of a helper method to handle the secondary 2-pointer algorithm for the two new strings. If the string was not a palindrome
the method would return a tuple of the current indexes of the two characters, else, it'll return a tuple of '-1, -1'. If the helper method returns a tuple of -1, -1 for either substring. We return True since the string is a palindrome if you remove one char


## Complexity
- Time: O(n)
- Space: O(1)

## Notes
After reviewing solutions, I realized that once you come upon chars that don't match. You shoould call the helper method with the two substrings and return true or false eliminating the need of initializing 3 strings and allows for more intuitive code
