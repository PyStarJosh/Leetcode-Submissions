# 0074. Search a 2D Matrix

**Difficulty:** Easy

**Topics:** Binary Search

**Link:** https://leetcode.com/problems/search-a-2d-array/

## Approach
This problem asks to return a boolean value when given a matrix of ascending order ints has the target value within it. I started the problem by decomposing the matrix into the base data structure which was an array of arrays. So, I understood at this point, I can implement
a binary search for the row containing the target value and implement binary search to find the value within the row meeting the O(log (m * n)) complexity.

  
## Complexity
- Time: O(log (m * n))
- Space: O(1)

## Notes
I learned another way to solve this problem by converting it into a flat array to reduce the lines of code. It's quite elegant and can be found in optimized_solution.py along with it's explanantion.
