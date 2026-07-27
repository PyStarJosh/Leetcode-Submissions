# 0018. 4Sum

**Difficulty:** Medium

**Topics:** Array, Sorting, Two-Pointer

**Link:** https://leetcode.com/problems/4sum

## Problem Statement
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

## Algo
My strategy for solving this problem was based around using two fixed array pointers that I'll use to subtract their array value from the target. Then, I'll implement a two sum algorithm to find the two remaining values needed to complete
the quadruplet. 

1. Sort the array
2. Initialize the first fixed pointer that goes from 0 to len(nums) - 3
3. Check if the element is a greater than zero and a duplicate of its previous value, if True, increment the value and continue
4. Initialize the second fixed pointer
5. Check if the element is a greater than the first pointer value + 1 and a duplicate of its previous value, if True, increment the value and continue
6. Calculate the difference variable that tracks what number is needed from our two sum algo to complete the quadruplet
7. Initialize the remaning two pointers that will traverse the remaining array elements for the final two values needed in the quadruplet
6. While the left pointer is less than the right pointer, calculate the total of nums[left] + nums[right] and compare it to the difference needed
7. If equal, append the 4 elements to res as a list, increment left pointer, decrement right pointer.
8. Check if the left pointer is less than right and a duplicate of it's last array value, if True, increment the value
9.  Check if the right pointer is greater than left and a duplicate of it's last array value, if True, decrement the value
10. If total > diff, decrement right pointer by 1
11 If total < diff, increment left pointer by 1
12. After the nested loops terminate, return res 2d array

## Complexity
- Time: O(n^3) -> Essentially 3 nested for loops
- Space: O(1) -> O(1) - Only constant variables initialized
