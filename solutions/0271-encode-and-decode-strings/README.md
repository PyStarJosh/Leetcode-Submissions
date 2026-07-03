# 0271. Encode and Decode Strings

**Difficulty:** Easy

**Topics:** Array

**Link:** https://leetcode.com/problems/encode-and-decode-strings/

## Approach
This problem requries you to encode a list of strings into one string and pass that string to a decode method which converts the string back into a list of strings.

I attempted to simply use ''.join() method with a delimiter, but it fails on test cases that use the delimiter in the string itself. I couldn't find the answer on my own, so I watched neetcode video on this problem and implemented a more efficient
solution than his by using ''.join() instead of s += str as s += str copies the existing string and creates a copy with the added string onto the end compared to ''.join which scans the iterable and allocates the right amount of space needed to
migrate once.

Algo:
1. Initialize the conjoined string with the length of the string and my chosen delimiter prefacing each string.
2. Initialize res array to capture strings and a index pointer starting at 0 that will represent the beginning of each string including str length and delimiter
3. While start index pointer less than len(s), we do the following.
4. Set a second pointer equal to start pointer which will be used to track the beginning of each actual string
5. Iterate through string until we come upon delimiter
6. Set the length by capturing the int value between the start and string pointer
7. Once we know where the string begins, we append the string to our res array
8. Update our start pointer to the next word
9. Return res when we are termination condition is met.
      
## Complexity
- Time: O(n)
- Space: On)

## Notes
I learned how to use f strings within the .join() method and that it is superior to the += operation for conjoining strings
