# 0075. Sort Colors

**Difficulty:** Easy

**Topics:** Array, Dutch Flag Algorithm

**Link:** https://leetcode.com/problems/sort-colors/

## Approach
This problem requries you to take a unsorted array of ints consisting of values; 0, 1, and 2 and sort them in-place using a one-pass algorithm with constant space.

I decided to implement the Dutch Flag Algorithm for this problem aas it meets the one-pass algorithm with constant space constraint.

Algo:
1. Initialize low = 0, mid = 0, high = n -1 variables to dissect the array into 4 sections.
  - low sits to the right of all 0 elements
  - mid represents the current element and elements between the two pointers
  - high sits to the left of all the 2 elements
2. Initialize while loop that iterates until mid > high
  - Once high < mid, the array has been sorted
3. If-elif-else statement to trigger appropriate actions for each potential element value at arr[mid]
  - If 0, array values at index mid and low are swapped with low and mid being incremented by 1
  - If 1, mid is incremented by 1 since they number falls within the middle of 0 and 2 naturally due to the algorithms nature
  - If 2, array values at index mid and high are swapped with high decremented by 1 with mid remaining the same for the purpose of re-checking.

## Complexity
- Time: O(n)
- Space: O(1)

## Notes
I learned the Dutch Flag Algorithm to solve this problem. It allows for you to sort an int array with 3 different elements in one pass with constant space. An alternative to this algorithm would be counting sort which is a 2 pass algorithm.
