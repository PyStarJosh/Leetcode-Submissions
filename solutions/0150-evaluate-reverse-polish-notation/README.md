# 0150. Evaluate Reverse Polish Notation

**Difficulty:** Medium

**Topics:** Array, Math, Stack

**Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation

## Problem Statement
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

## Algo
My strategy for solving this problem was to use a stack to append the numerical values and do computations on the two top values when an operand is passed during traversals. This solution allows us to keep the running result on the top of the stack
allowing for in-order computations. 

1. Initialize a stack for final result and set (holds operand values for O(1) lookup)
2. Iterate through the given array
3. If the current token is an operand, pop() the top value and move to the match statement for the appropriate operation applied to the new top of the stack. (division must truncate to 0, so use int() as this slashes the decimal portion of the float truncating towards 0
4. Else, append the numerical string to the stack as an integer
5. Return remaining element in the stack holding the final result

## Complexity
- Time: O(n) -> Traversed given array once
- Space: O(n) -> As stack grows with each int value traversed
