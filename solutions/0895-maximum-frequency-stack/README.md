# 0895. Maximum Frequency Stack

**Difficulty:** Hard

**Topics:** HashTable, Stack

**Link:** https://leetcode.com/problems/maximum-frequency-stack

## Problem Statement
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

## Algo
My strategy for solving this problem was to keep track of the current frequencies reached by the elements and make them to their respective elements using a HashMap of stacks. 
This allowed me to simply acquire the frequency of a value and append it to it's respective frequency group. Appending the elements allows me to collect them in a ordered manner,
so I can simply access the last element to get the value closes to the top.

1. Initialize frequency HashMap of integers, HashMap of stacks, and a max frequency variable 
2. In push method, track increment the current frequency value for the value passed, check if it's the new max frequency and append the value to the stack
   representing the current frequency
3. In the pop metho, access the stacks HashMap at the key representing the max frequency seen so far and pop() from it to get the highest frequency element
4. Check if that stack is empty, if so, decrement max frequency by 1
5. Return the max frequency element

## Complexity
- Time: O(1)
- Space: O(1) 
