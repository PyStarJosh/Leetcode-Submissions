# 0015. 3Sum

**Difficulty:** Medium

**Topics:** Array, Sorting, Two-Pointer

**Link:** https://leetcode.com/problems/3sum/

## Problem Statement
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Algo
My strategy for solving this problem is to utilize a 2-pointer algorithm that employs the use of 3 pointers. The core of my algorithm is a sorted
array as this allows for me to lock the left pointer on a value and treat the two remaining pointers and values like the 2sum LeetCode problem. However, the problem
states duplicate triplets nor duplicate values can be added to each triplet. The second constraint of duplicate values is handled by my while loop as it terminates when my mid and right 
pointer touch each other. For the duplicate triplet value, we have to check for consective duplicates and increment j until a new value is found. This gives us the correct triplets that 
fit the constraints provided, so we can finally return our matrix of triplets.

1. Init result list
2. Sort the input array
3. Iterate through array via index
4. Check if left pointer is a duplicate element, if so, skip it.
5. Init the 2 remaining pointer; mid and right. mid is left + 1 and right is length of input array - 1
6. Implmeent two pointer while loop
7. Adjust pointers based on calculated total sum of 3 elements
8. Handle duplicate triplets by incrementing mid until you find a new element 
9. Return results matrix

## Complexity
- Time: O(n^2) -> we nust traverse the array n * n time;
- Space: O(n) -> dependent upon sorting algo, but python uses PowerSort
