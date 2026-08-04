# 0739. Daily Temperatures

**Difficulty:** Medium

**Topics:** Monotonic Stack, Array, Staff, Stack

**Link:** https://leetcode.com/problems/daily-temperatures

## Problem Statement
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for
which this is possible, keep answer[i] == 0 instead.

## Algo
My strategy for solving this problem was to use a monotonic stack that held the current temps indexes in a decreasing temp order until a warmer temp was found in the array. Once a warmer temp was found, the top temp would be popped and it's index
in the result array would be given the difference between the current warmer index minus that was popped from the stack. This step is repeated until the stack is empty or the top value in temps array is greater than or equal to the current idx in temp.
Once this condition is met, we simply append the new warmer date onto the stack

1. Initialize a result array of size n and an empty stack
2. While the stack has values and temps[index at top of the stack] is less than temps[current index], pop() from stack and reassign res[popped index] to current index minus popped index
3. When the while loop terminates, put current index onto stack
4. When the for loop terminates, return result array
   
## Complexity
- Time: O(n) -> 1 pass of given array
- Space: O(n) -> 2 n size data structures initialized
