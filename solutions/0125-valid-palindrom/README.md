# 0125. Valid Palindrome

**Difficulty:** Easy

**Topics:** Two Pointer

**Link:** https://leetcode.com/problems/valid-palindrome/

## Approach
This problem asks you to return true if the string given is a palindrome. I implemented a two pointer algorithm to solve this problem. I started by cleaning the string using python's 're' module's 're.sub(^-a-zA-Z0-9], '', s' function and the '.lower()' method, so it only contained alphanumerical values followed by 
initializing pointers for the front and end of the string index values. I will increment each iteration of the while loop to compare their corresponding values and if the values were different, my functions would return False, else the while
loop would finish and return True.

## Complexity
- Time: O(n)
- Space: O(1)

## Notes
I didn't know about the re module in python, so I initially thought to implement two methods containing a-z and 0-9 to compare the values against, but I knew their must be a more succinct way of cleaning the string and I did some research to discover the re
module. 
