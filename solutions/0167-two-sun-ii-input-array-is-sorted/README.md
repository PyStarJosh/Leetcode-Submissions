# 0167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium

**Topics:** Array, Two-Pointer

**Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Problem Statement
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add 
up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

## Algo
My strategy for solving this problem was problem was to employ a 2-pointer algorithm that has one pointer at the end and one pointer at the beginning of the array.
This allowed me to get the sum of 1 large and 1 small element in the array and increment and decrement the pointers dependant upon the total compared tothe target.
If the total was larger than the target, decrement the right pointer and if the total is larger than the target increment the left pointer. I adopted this algorithm from the range resizing characteristic of binary search.

1. Initiliaze 2 pointers; left and right
2. Begin the while loop that terminates when left pointer is greater than or equal to right pointer
3. Calculate the sum of the two pointer values in the array
4. Compare them to the target
5. If target == total, return left + 1 and right + 1 as an array of length 2
6. if target > total, increment left pointer to next smallest value
7 Else, decrement the right pointer to the next largest value

## Complexity
- Time: O(n) -> traverse given array
- Space: O(1) -> only 2 constant variables created
