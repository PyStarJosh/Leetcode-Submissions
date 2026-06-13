# 0027. Remove Element

**Difficulty:** Easy

**Topics:** Array

**Link:** https://leetcode.com/problems/remove-element/

## Approach
This problem asks to modify an array of nums in place and return the number of elements that are not equal to the target val passed into the function:

So, I  thought of comparing each num in the array against the target value and incrementing each time it is different to track the number of different elements. In addition, I utilized in-place modification to push the passed value into the last indexes of the array allowing for the 
non-target values being first in the array. 

## Complexity
- Time: O(n)
- Space: O(1)

## Notes
None
