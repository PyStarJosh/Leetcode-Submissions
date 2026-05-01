# 0035. Search Insert Position

**Difficulty:** Easy

**Topics:** Binary Search

**Link:** https://leetcode.com/problems/search-insert-position/

## Approach
This problem asks to return a index of the target value within an array. However, you should return the index at which the value would be inserted into the array. 
I simply implemented a binary search algorithm that returns 'mid' when the target is found and returns left when the target is not found. The left variable as
it always resides at the smallesst index that hasn't been ruled out yet.

## Complexity
- Time: O(log n)
- Space: O(1)

## Notes
From drawing the algo on paprt, I knew after to walkthroughs that left would give me the correct index for insertion, but I couldn't figure out why. Until, I noticed that the while loop break statment
left is always 'right + 1' and this means left is at an index where everything to the right has been proven to be too big and everything to the left has been proven to be too small.
