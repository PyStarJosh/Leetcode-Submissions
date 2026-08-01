# 0232. Implement Queue using Stacks

**Difficulty:** Easy

**Topics:** Stack, Design, Queue

**Link:** https://leetcode.com/problems/implement-queue-using-stacks

## Problem Statement
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

## Algo
My strategy for solving this problem was to use two arrays to emulate the functions of a queue; one array would handle the put operation and keep track the appended elements and the other will keep track of the top element for peek and pop operations.

1. Initialize 2 arrays; tail array and head array
2. For put(), simply append to the tail array
3. For peek(), check if the head array is empty, if so, pop every element from the tail array and append it to the head array
4. For pop(), call peek() to ensure head array contains current head, if so, simply pop from the output array as the head is in the last position
5. For empty(), check if both head array and tail array are empty, if so, return True, else, False

## Complexity
- Time: O(1) amortized -> LL operations are o(1) except for peek which is amortized O(1) as the need to pop every element from input decreases over time.
- Space: O(n) -> 2 arrays initialized
