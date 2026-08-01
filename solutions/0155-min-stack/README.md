# 0155. Min Stack

**Difficulty:** Medium

**Topics:** Stack, Design

**Link:** https://leetcode.com/problems/min-stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

## Algo
My strategy for solving this problem was to utilize two stacks; one containing every element acting as the main stack and the second stack acting as the min stack only carrying the minimum value found so far. This allows me to peek at the top of the
min stack array for the current minimum value in the stack while still providing the ability to pop and peek from the original array as normal. I choose my implementation over the stack containing list of the appended value and current minimum value in the array,
because it felt less intuitive and more memory intensive compared to my algorithm as in best average case scenarios the mins stack contains less than n elements while maintaining O(1) time complexity.

1. Initialize two stacks (dynamic arrays)
2. For push, append to the end of the main stack, but only append to the min stack if the value being appended is less than or equal to the current top value of the min stack or the min stack is empty
3. For pop, pop() from the main stack and pop() from the second stack if the returned popped value equals the min stack top value
4. For top(), return the top of the main stack
5. For getMin(), return the top of the min stack

## Complexity
- Time: O(1) -> constant operations all around
- Space: O(2n) -> O(n) - 2 stacks; 1 size n and the other potentially size n
