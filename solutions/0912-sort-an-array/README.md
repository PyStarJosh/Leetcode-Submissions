# 0912. Sort an Array
**Difficulty:** Easy

**Topics:** Array, Sorting Algorithms

**Link:** https://leetcode.com/problems/sort-an-array/

## Approach
This problem asks you to sort an array of numbers in ascending order in O(n log n) time complexity.]
1. I opted to employ merge sort as my sorting aglgorithm as it has a true time complexity of O(n log n) in any case.
2. I implemented the divide and conquer sorting algorithm using a recursion and a helper method
3. I started with my recursive base case which stops when the passed nums argument has a length of 1 or less
4. Then, I created varibles to track the middle index and assign the respective values to the left and right array
5. I recursively split the main array into two arrays the left and right array until the base case was met.
6. I would then call my helper method '_merge' the sorted left and right arrays until the final result once every call is popped of the stack.
7. The helper method iterates through the index of both the left and right array to compare their values and assign the values to the correct main array position
8. Finally, my helper catches any remaining numbers that may be left in the left or right array.

## Complexity
- Time: O(n log n)
- Space: O(n)

## Notes
I learned how to implement merge sort from YouTube.
