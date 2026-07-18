# 0036. Valid Soduku

**Difficulty:** Medium

**Topics:** Array, HashSet

**Link:** https://leetcode.com/problems/valid-sudoku/

## Problem Statement
This problem asks to return a boolean value that represents whether the provided Sudoku board is valid. 

## Algo
My strategy for solving this problem is to utilize HashMap of sets to keep track of the values of each row, column, and sub-box. Then, I'll traverse the entire matrix since it is of a fixed size meaning O(n^2) time complexity is ubobtainable.
I'll check if the current element is in any of it's respective row, column, or sub-box sets. My algo will return False if the element already exist or add the element to it's respective key's in the HashMaps. 

1. Initiliaze 3 HashMaps with set values
2. Iterate through the matrix 
3. Check if current element is a valid input
4. Calculate the element's respective sub-box
5. Check if element exist in any of it's respective key in each HashMap
6. If it already exist, return False, else add the element to it's respective key in each HashMap
8. If the loop finishes, return True

## Complexity
- Time: O(81) -> O(1) - Each element
- Space: O(243) -> O(1) - Each HashMap has a size of 81 elements

## Notes
