# 0229. Majority element II

**Difficulty:** Medium

**Topics:** Boyer-Moore Voting Algo, Arrays

**Link:** https://leetcode.com/problems/majority-element-II/

## Problem Statement
Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.
Follow up: Could you solve the problem in linear time and in O(1) space?

## Approach
Given this problem's auxiliary space constraint, I chose to use Boyer-Moore Voting algo to solve this problem as
it allows to find the majority element in an array in O(n) time while using O(1) auxiliary space.

**Boyer-Moore Voting Algo**: This algorithm takes advantage of that fact that a majority element will take up most of the array.
You can take advantage of this by incrementing and decrementing the count of the current majority element because the current majortiy element is not the true majority element if it's count reaches 0.
Finally, the element that finishes the iteration with a non-zero count is the majority element.

Boyer-moore Voting Algo will be the basis for my approach, but it must be modified as the problem ask for elements that occur more than 
n/3 times in the array. So, here's how I adjusted the algo to this this problem:

1. Init 2 count variables to 0
2. Init 2 candidate variables to None
3. Iterate through the given int array
4. If the current element equals candidate 1, increment count1 by 1
5. If the current element equals candidate 2, increment count2 by 1
6. If candidate1 equals 0, set candidate1 to the current element and reset count to 1
7. If candidate2 equals 0, set candidate2 to the current element and reset count to 1
8. Else decrement count1 and count2 by 1 as num did not equal either candidate.
9. Verify the occurrences of the two candidates.
10. If candidates count is greater than length of array divided by 3, append candidate to result array
11. Return result array

## Complexity
- Time: O(n): two traverses of the given array of size n
- Space: O(1): We utilize constant variables to determine two majority elements in the array

## Notes
