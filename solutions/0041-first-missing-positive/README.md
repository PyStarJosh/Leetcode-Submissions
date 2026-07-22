# 0041. First Missing Positive

**Difficulty:** Hard

**Topics:** Array, Cycle Sort, In-place modification, Index Mapping

**Link:** https://leetcode.com/problems/first-missing-positive/

## Problem Statement
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

## Algo
My strategy for solving this problem was to utilize cycle sorting and index mapping to reconstruct the array where each value is at index value - 1 with values less than 1, out of place values, and values greater than length of the array left behind to mark the missing 
positive number.

1. Iterate through the indices of the given array
2. Use a while loop to swap values that terminates when a value is in it's correct index or the value < 1 or > n.
3. Initialize a val variable tracking the current value
4. Swap the current array index with the array index at value - 1
5. Once the array is reconstructed, iterate through the array again to look for the missing positive number.
6. If nums[idx] is not equal to idx + 1. The missing positive int is idx + 1
7. If the second loop doesn't terminate early, return length of the array + 1

## Complexity
- Time: O(n)
- Space: O(1)
