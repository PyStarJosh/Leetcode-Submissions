# 0735. Asteroid Collision

**Difficulty:** Medium

**Topics:** Array, Stack, Simulation, Staff

**Link:** https://leetcode.com/problems/asteroid-collision

## Problem Statement
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Algo
My strategy for solving this problem was to use a stack to collect every right moving asteroid and left moving asteroid if they arrived upon an empty stack, the stack with a negative top element, or the left moving asteroid collided it's way
through the entire stack. Otherwise when left moving asteroids are encountered, we get the abs value and compare it to the current top value. If the left moving asteroid is bigger, we pop the right moving asteroid from the stack and continue compare each sequential top until one of the other conditions are met, else if the top element and
left moving asteroid are equal, we pop() the top element and move to the next asteroid, if the top element is larger, we simply don't append the left moving asteroid and continue with the next element in asteroids.

1. Initialize a stack
2. Iterate through the asteroids array
3. While res has values and the current asteroid is less than 0 and the top element is greater than zero, we will calculate the collisions, else, put the current asteroid onto the stack
4. Compare the current right moving asteroid size to the absolute value of the left moving asteroid size
5. If left moving asteroid is larger, pop() top element and repeat comparisons with new top()
6. If they are equal in size, pop() the top element and break the while loop as both asteroids are destroyed
7. Else, the top element (right asteroid) is larger than left moving asteroid, so simply do nothing and move to the next element in asteroids
8. Return stack

## Complexity
- Time: O(n) -> 2 passes of asteroids
- Space: O(n) -> stack of size n
