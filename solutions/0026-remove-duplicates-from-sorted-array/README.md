# 0026. Remove Duplicates from Sorted Array

**Difficulty:** Easy

**Topics:** Array, Two Pointer

**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Problem Statement
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

## Algo
My strategy for solving this problem was to use a two pointer algo to sort the unique k elements to the front of the array while keeping one pointer on the last unique element. I would achieve this by comparing two sebsequent values for equivalence,
if they were equal increment the right pointer to the next element until I found a different element. Once the different element is found, we increment the left pointer to the new index space for the lastest unique element followed by swapping the values at 
the left pointer index and right pointer index. At the end of the array traversal, we simply return my left pointer int value + 1 to represent the length of unique elements.

1. Initialize k = 0
2. Iterate through the array starting at 1 and ending at array length - 1
3. Compare the values at arr[k] == arr[j]
4. If different, increment l and set arr[k] = arr[j]
5. Repeat steps 3 and 4 until loop terminates
6. Return k + 1

## Complexity
- Time: O(n)
- Space: O(1)
