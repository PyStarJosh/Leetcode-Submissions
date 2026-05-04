# 0344. Reverse String

**Difficulty:** Easy

**Topics:** Two Pointer

**Link:** https://leetcode.com/problems/reverse-string/

## Approach
This problem asks you to reverse a string given in the form of an array of chars with the constraint being your solution must maintain O(1) space complexity. For my solution, I implemented a two pointer algorithm by saving two variables,
one pointing to index 0 and the second pointing to 'len(array) - 1'. I used these variables in my while loop condition stating the while loop should run while 'front < back'. Inside the while loop, I would set s at index 'front' to s at index
'back' and vice versa for s at index 'back' follwed by incrementing front by 1 and back by -1. This allows me to traverse the array in O(n) runtime complexity while achieving the constraint of O(1) space complexity.

## Complexity
- Time: O(n)
- Space: O(1)

## Notes
I initially used a if statement to check if array value at front and back were equal to skip the iteration, but I noticed my solutions didn't apply this if statement. So, I did research on why many choose to omit the if statement and it's 
related to redability as the if statement doesn't bring noticable runtime improvements, so the more readable code is the better choice.
