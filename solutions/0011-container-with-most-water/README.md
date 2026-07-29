# 0011. Containers with Most Water

**Difficulty:** Medium

**Topics:** Array, Greedy, Two-Pointer

**Link:** https://leetcode.com/problems/container-with-most-water/

## Problem Statement
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

## Algo
My strategy for solving this problem was to use a 2 pointer algorithm to iterate through the array while computing the area at each iteration to keep track of the max area seen. I noticed from the example that if two verical lines were not equal
in height the shorter height was used to compute the area as the problem states no slanting the container, so I want to use min to keep track of the shorter line and multiply it by the number of elements between from the right line to the left line being compared
, which is essentially right pointer minus left pointer

1. Initialize left and right pointer along with res variable to capture max array
2. Iterate through the matrix while left is less than right
3. Calculate the current area between left and right pointer, and check if it's higher than the current max, if so, assign the current value to the max area variable
4. Compare the values at the left pointer and right pointer, the lower value gets incremented (left) or decremented(right)
5. Return max area variable

## Complexity
- Time: O(n) -> 1 pass of given array
- Space: O(3) -> O(1) - Only constant variables initialized
