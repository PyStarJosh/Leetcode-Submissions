# 0069. Sqrt(x)

**Difficulty:** Easy

**Topics:** Binary Search, Newton-Raphson iteration

**Link:** https://leetcode.com/problems/sqrtx/

## Approach
This problem asks to return the sqrt of a given int. I researched how sqrt's worked under the hood to come upon
Newton-Raphison method (r + n/r) / 2 that allows you to find the sqrt of any number in log log n time complexity. I started by initializing
res to equal the given int fillowed by initializing a while loop with the condition 'res * res > n', so it ran until we found
'res * res <= n'. This gave me the ability to utilize iteratively decrement the res value until we reach the floor sqrt at this point I'll return res.

## Complexity
- Time: O(log log n)
- Space: O(1)

## Notes
I initally utilized 'abs(res * res - x) < 0.5' to evaluate if the floor sqrt int was found, but I found my current solution to be simpler
with improved readability/simplicity
