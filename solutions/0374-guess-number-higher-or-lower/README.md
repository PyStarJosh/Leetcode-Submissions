# 0374. Guess Number Higher or Lower

**Difficulty:** Easy

**Topics:** Binary Search

**Link:** https://leetcode.com/problems/guess-number-higher-or-lower/

## Approach
This problems calls for you to utilize an API call that returns 3 values 0, 1, and -1. These int values represent correct, too low, and too high. So, I calculated 'mid' as usual in binary search
with the caveat that 'left = 1', and 'right = n' since we were dealing with the values directly. Nonetheless, you simply pass mid into the 'guess(num: int)' and appropriately adjust your mid variable based on the response
and finally return the 'mid' when 'guess(mid)' returns 0

## Complexity
- Time: O(log n)
- Space: O(1)

## Notes
None
