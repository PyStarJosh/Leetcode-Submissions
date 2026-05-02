# 0001. Two Sum

**Difficulty:** Easy

**Topics:** HashMap

**Link:** https://leetcode.com/problems/two-sum/

## Approach
This problem asks you to return the indexes of two elements in an int array that equals the target number. I utilized python's HashMap to take advantage of the O(1) search while iterating through the loop via indexes and subtracting the target from the current array element followed by checking if the result was a key in my HashMap. If the result is in the HashMap, return the current index variable value with the value of the HashMap key. However, if the key is not in my HashMap, I simply add the element to the HashMap with it's index value as the key for later use.

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
None
