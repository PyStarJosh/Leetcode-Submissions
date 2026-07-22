# 0088. Merge Sorted Array

**Difficulty:** Easy

**Topics:** Array, Two Pointer, Sorting

**Link:** https://leetcode.com/problems/merge-sorted-array/description/

## Problem Statement
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

## Algo
My strategy for solving this problem was to use my understanding of merge sort to replicate the same algorithm for this problem. However, I discovered the arrays must be traversed in reverse from largest to smallest to allow for easier insertion into
the main array as we just have to overwrite the placeholder 0s. In addition, nums1 and nums2 are different lengths, so it's important to keep track of the nums2 when decrementing to prevent IndexOutofBoundsErrors. Once you have the while loop set up, you compare the two values using your pointers
insert the larger value into the main array overwriting the current index in the main array.

1. Initiliaze 3 pointers
2. Initialize while loop for nums2 pointer
3. Check if left array pointer is >= 0 and if nums1 pointer value is greater than nums2 pointer value.
4. Insert the larger value into the main array at the third pointer and decrement the point inserted.
5. Decrement the third pointer
6. Repeat until both the nums1 and nums2 pointers are below zero indicating both arrays were traversed.

## Complexity
- Time: O(m + n) -> traverses nums1 of size m and nums 2 of size n
- Space: O(1) -> only 3 constant varibales initialized
