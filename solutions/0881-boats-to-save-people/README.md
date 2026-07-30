# 0011. Boats to Save People

**Difficulty:** Medium

**Topics:** Array, Greedy, Two-Pointer, Sorting

**Link:** https://leetcode.com/problems/boats-to-save-people

## Problem Statement
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

## Algo
My strategy for solving this problem was to use a greedy 2 pointer algorithm to iterate through an sorted array while computing the weight of the heaviest and lightest person each iteration to maximize the chance of a boat carrying two people.
If both individuals weighed less than the limit, we would increment/decrement both pointers, but if they're weight exceeded the boat weight limit, the right pointer would be decremented as won't to try decrease the combined weight to find a pair that can be transported together.

1.Check if len(arr) = 1, if True, return 1 for quick O(1) termination 
2. Initialize left = 0 and right pointer at len(arr) - 1 along with boats = 0
3. Sort the array using .sort()
4. While left < right, add the weights of each individual, increment boat by 1 and compare them to the boat limit.
5. If pair weight exceeds limit, decrement right by 1, else, increment left by 1 and decrement right by 1
6. Return boats

## Complexity
- Time: O(n log n) -> power sort has O(n log n) time complexity
- Space: O(n) -> dependent on sorting algo
