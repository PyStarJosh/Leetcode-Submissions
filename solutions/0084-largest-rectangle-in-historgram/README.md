# 0084. Largest Rectangle in Histogram

**Difficulty:** Hard

**Topics:** Array, Stack, Monotonic Stack, Range Min/Max Query

**Link:** https://leetcode.com/problems/largest-rectangle-in-histogram

## Problem Statement
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

## Algo
My strategy for solving this problem was to use a monotonic stack that keeps track of the histogram bars height and index for future area calculation. While traversing the list, we append the current bar's height and index
until a smaller height is passed. The top element of the stack is popped, the height and index used to calculate the area, the area is compared to the current max area and the popped bar's index
is saved as the new start for the current bar to be appended when a shorter bar is passed. This repeats until the entire array has been traversed. At the end, we may still have leftover elements as the array did not contain an bar height shorter than
the remaining heights after their respective indexes, so we run a while loop to pop the top element and compute the area for max comparison against the max area. For the final pass, we will use the length of the original array as the current index.

1. Initialize an stack and set max area to 0
2. Enumerate through heights, set start to current index
3. While stack is populated and the top value is greater than the current height, pop() the top value, compute it's area, compare it against max, and set start to the index of the popped element
4. Once done enumerating, If stack is still populated, pop() elements and compute their area for comparison until stack is empty
5. Return max area variable

## Complexity
- Time: O(n) -> 1 enumeration of given array
- Space: O(n) -> Stack of potential size n is initialized
