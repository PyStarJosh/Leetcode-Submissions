# 0682-baseball-game

**Difficulty:** Easy

**Topics:** Stack

**Link:** https://leetcode.com/problems/baseball-game/

## Approach
The provided list contains string of ints, '+', 'C', and 'D', the ints are the operands for the 3 operations. Therefore, I implemented a list to keep track of every int from the list.
I understood that we would iterate through the list and store the int values and perform the operations when an op char was passed. However, the ints in the list were stored as strings, so I
decided to create a if-elif-else statement that catch the operations first resulting in my else statement catching and converting the value from string to int. Finally, I decided to simply
utilize the built-in python function 'sum' to return the sume of the list for code conciseness. 

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
LeetCode solution implements a stack for solving this problem, but this solution is redundant for python as emulating the operations and constraints of a stack will add additional steps for
the '+' operation as you'll have to pop and store the last item, peek at the new top, add them, append the old top back on and append the result of summing them. It's simplier and requires less
steps to simply utilize python's list indexing abilities to add 'list[-1] + list[-2]'
