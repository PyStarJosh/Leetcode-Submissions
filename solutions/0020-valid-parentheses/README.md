# 0035. Search Insert Position

**Difficulty:** Easy
**Topics:** Stack
**Link:** https://leetcode.com/problems/valid-parentheses/

## Approach
This problem asks to return a boolean value when given a string of brackets. An input string is valid if:

  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.

So, I instantly thought of a stack for this solution as it will allow me to append opening brackets and pop them from the top when I came across a closing bracket. 
This would allow me to save the popped opening bracket and compare it to the current char(closing brackets). However, I faced the issue of comparing the two values since 
they're not identical, so I thought of the idea to use a hashmap to connect the values. At this point, the comparison would validate rule 1 and 2, but number 3 required the
tracking of the stack size to ensure every closing bracket had a open bracket and this was implemented using simple if statements.

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
Initially, I missed the test case where s = '}' with the only char being a closing value which returned an error as I attempted to pop off an empty stack. However, I fixed this issue with
a simple if statement.
