# 0394. Decode String

**Difficulty:** Medium

**Topics:** String, Stack, Recursion

**Link:** https://leetcode.com/problems/decode-string

## Problem Statement
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

## Algo
My strategy for solving this problem was to use a stack to hold all values until my traversal came upon a closing square bracket. At this point, we will first get the current string by popping chars until we reach a opening bracket. Then, we will pop
the opening bracket and get the current number of times via popping until a the stack is empty or the value is not longer a digit. Finally, we'll convert the current num to an int and multiply it by the string and join the stack values to return the decoded string.

1. Initialize the stack
2. Iterate through the string, checking for closing brackets, else pop() valet onto bracket
3. Once a closing bracket is reached, pop the current char at the top of the stack and append it to the empty current string variable
4. Once a opening bracket is reached, pop it and begin appending the numerical values that sit on the top of the stack until the stack is empty or the top value is no longer a digit.
5. Convert the current number variable to a int and multiply the current string by it
6. After the for loop terminates, join the stack values and return the string

## Complexity
- Time: O(n) -> 1 pass of given array
- Space: O(n) -> O(1) - 1 stack initialized
