# 0704. Binary Search

**Difficulty:** Easy

**Topics:** Binary Search

**Link:** https://leetcode.com/problems/binary-search/

## Approach
The project simply instructs you to find a target value's index in an array with O(log n) runtime complexity. So, I implemented binary search to eliminate half of the array each iteration achieving the O(log n) runtime complexity.

## Complexity
- Time: O(log n)
- Space: O(1)

## Notes
Remember when initializing 'midpoint_index' to utilize 'start_index + (end_index - start_index) // 2' to decrease the chances of an overflow error. 
