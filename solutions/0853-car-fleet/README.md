# 0853. Car Fleet

**Difficulty:** Medium

**Topics:** Array, Staff, Sorting, Monotonic Stack

**Link:** https://leetcode.com/problems/car-fleet

## Problem Statement
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

## Algo
My strategy for solving this problem was to combine the all the cars' positions and speeds into a tuple of tuples and reverse them, so
the furthest starting car is first in the tuple. I would iterate through the tuple and calculate the time it'll take for a car to make it to the target starting with the furthest car.
I add this value to the stack for future comparison as any future vehicle will be coming from behind the current top element, so if the car computed travel time is greater than the top of the stack car,
it will be apart of another fleet.

1. Combine the cars' positions and speeds in a reverse sorted 2d tuple
2. Iterate through the array computing the travel time
3. If the stack is not empty and the current car travel time < next car travel time, append the new car to the array to represent an additional fleet
5. When the for loop terminates, return length of stack as it length represents the number of fleets

## Complexity
- Time: O(n) -> 1 pass of given arrays, 1 pass of 2d tuple
- Space: O(n) -> 2d tuple and stack that can grow to size n
