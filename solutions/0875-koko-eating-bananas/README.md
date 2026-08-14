# 0875. Koko Eating Bananas

**Difficulty:** Medium

**Topics:** Array, Binary Search

**Link:** https://leetcode.com/problems/koko-eating-bananas

## Problem Statement
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

## Algo
My strategy for solving this problem was to use implement an binary search algorithm based around the range from 1 to the maximum value in piles. This strategy originated from recognizing that the answer for k would be within the piles array
as the largest value in the array would 100% finish the piles within h hours. So, it's the job of the binary search to find potentially smaller values that can finish at the same time or faster. We would implement this by taking the range of piles and dividing it by 2.
Next, we'll increment through piles incrementing a total time variable that will be compared against given h variable. If the total time is less than or equal to h, we will add this new smaller value as our current answer and decrement the right pointer to
this value - 1. Once the left is greater than right, we return the current answer variable.

1. Initialize left to 1 and right pointer to max value in piles
2. Iterate through the matrix while left is less than or equal to right pointer value
3. Calculate the current k value to check, initialize total time variable to 0 and iterate through each pile adding the floor division result between pile and k
4. Compare the values of total time and h after the piles traversal, if total time is less than or equal than h, set answer variable to the current k value and set right to k minus 1, else set left to k + 1 
5. Once while loop terminates, return answer variable

## Complexity
- Time: O(n logm) -> 1 pass of piles (O(n) per while loop iteration (O(logm)
- Space: O(1)-> Only constant variables initialized
