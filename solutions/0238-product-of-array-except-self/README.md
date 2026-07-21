# 0238. Product of Array Except Self

**Difficulty:** Medium

**Topics:** Array, Prefix Sums

**Link:** https://leetcode.com/problems/product-of-array-except-self/

## Problem Statement
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. You must write an algorithm that runs in O(n) time and without using the division operation. 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

## Algo
My strategy for solving this problem was to utilize prefix and suffix sums algorithms to track the products of elements to the left and right of the ith element providing the correct answer in O(n) time with O(1) space complexity since I saved
intermediate products in the results array.

1. Initialize a result array of size n with placeholder values of 1 to prevent uneccessary resizing resulting in a clean O(1) via in-place changes.
2. Set prefix to 1
3. Traverse the array
4. Assign res[idx] to prefix as we are getting populating it wirh nums[:idx] products
5. Multiply prefix by nums[idx], this is done at the end of the loop as it will lag behind by one index when assigning the suffix value to res[idx]
6. Once finished with prefix sums, initialize suffix to 1
7. Traverse the array backwards
8. Multiply res[idx] by suffix to get the final value 
9. Multiply suffix by nums[idx] to ensure res[idx] is multiplied by nums[idx + 1:]

## Complexity
- Time: O(81) -> O(n) - 2 traversals of given array of size n
- Space: O(243) -> O(1) - In-place modification of elements
