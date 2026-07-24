# 0013. Roman to Integer

**Difficulty:** Easy

**Topics:** Array, HashMap, Two-Pointer

**Link:** https://leetcode.com/problems/roman-to-integer/

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

## Algo
My strategy for solving this problem is to utilize HashMap of sets to keep track of the roman numeral values for use when traversing the array later. I would traverse the array while
checking two values at once to check for the unique cases where 

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
