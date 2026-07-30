# 0042. Trapping Rain Water

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Stack, Two-Pointe

**Link:** https://leetcode.com/problems/trapping-rain-water/

## Problem Statement
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Algo
My strategy for solving this problem was to use a 2 pointer algorithm to iterate through the array from the start and end of the array tracking the current smaller peak as this gives us the shortest current peak of the range. We use this as a reference
to subtract the next elevation values by until a value greater than the current shortest peak is crossed. This now updates the bounds of this internal range and we use the new walls as reference to subtract the intermediary elevations from until our pointers collide.

1. Initialize units = 0, left pointer = 0, right pointer = len(arr) - 1, left_max = 0, right_max = 0
2. Iterate through the matrix while left is less than right
3. Find the shorter peak for future elevation comparison
4. If the current larger value is greater than that side's max, update that side's max to the current value, if not, subtract that value from the max
5. return units

## Complexity
- Time: O(n) -> 1 pass of given array
- Space: O(1) -> O(1) - Only constant variables initialized
