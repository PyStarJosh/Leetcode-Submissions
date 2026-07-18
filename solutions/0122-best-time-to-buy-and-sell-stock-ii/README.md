# 0122. Best Time to Buy and Sell Stock II

**Difficulty:** Medium

**Topics:** Array

**Link:** [https://leetcode.com/problems/longest-common-prefix/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)]

## Problem Statement
This problem asks to return the maximum profit that you can achieve by buying and selling stock one share of stock at a time.

## Algo
My strategy for solving this problem is to find out when the price changes positively between days, so I can buy the stock. Then, I will sell the stock and calculate the difference to add into my profit.

1. Initiliaze res to 0
2. Iterate through the array starting at 0 and ending at the index length of array minus 2
3. Calculate the difference in prices between the two days
4. If the difference is positive, add it to res variable
5. Repeat steps 3 and 4 until loop terminates
6. Return res

## Complexity
- Time: O(n)
- Space: O(1)

## Notes
I'm pretty sure you can make the algo more efficient by using a while loop to keep track of the trend of prices over numerous days to reduce the constant buying and selling of stocks each day. Although, given the small array sizes used for
this problem's test cases, the performance increase is negligible.
