# 0189. Rotate Array

**Difficulty:** Medium

**Topics:** Array, Two-Pointer, Math

**Link:** https://leetcode.com/problems/rotate-array

## Problem Statement
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

## Algo
My strategy for solving this problem was using array reversals to shift the k elements to the front followed by sorting 0 to k - 1 and k to n - 1 to reorder the seperate sections based on k. It's important to understand that an array can
only be rotated n times, so we can take k % n to get our true number of rotations. This is important as it allows us to utilize k as a pointer to reverse and rotate our array when the given value exceeds n.

1. Calculate k %= n
2. Check if k == 0, if True, return as no rotations are needed
3. Reverse the entire array from 0 to n - 1
4. Reverse the array from range 0 to k - 1
5. Reverse the array from range k to n - 1

## Complexity
- Time: O(2n) -> O(N) - 2 complete traversals of n sized array
- Space: O(1) -> O(1) - In-Place Modification
  
## Notes
When a set of values are bounded by the length of the array utilize modulos math for proper indexing
