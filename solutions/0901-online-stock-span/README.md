# 0901. Online Stock Span

**Difficulty:** Medium

**Topics:** Stack, Design, Monotonic Stack

**Link:** https://leetcode.com/problems/online-stock-span

## Problem Statement
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

## Algo
My strategy for solving this problem was to use a decreasing monotonic stack that keeps tracks of the prices in descending order and their correlated price span. My algorithm
will add the values correlated span when a larger value is inputted for price. At this point, I will pop the list from the stack, but keep a pointer to it's span to add to the
current span of the larger value. This will give me the overall span for the current value. If the new passed value for price is smaller, it fits within my decreasing monotonic stack, so we simply append
it's value and span onto the stack.

1. Initialize a dynamic array to act as decreasing monotonic stack
2. While the stack is not empty and the passed price argument is larger than the current top value, pop the top value and it's span and increment the current span with the value's correlated span
3. Else, simply append the passed price value and it's corresponding span value
4. Return span

## Complexity
- Time: O(n) -> 1 pass of stack in worst case scenario
- Space: O(n) -> initialized stack can grow to size n (n representing price, span pairs)
