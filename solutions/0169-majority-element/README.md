# 0169. Majority Element

**Difficulty:** Easy

**Topics:** Array, HashMap

**Link:** https://leetcode.com/problems/majority-element/

## Approach
1. Initialize Defaultdict to store num as key and its number of occurrences within the nums array as the value
2. Iterate through the nums array
3. At each pass the current num value is passed into the defaultdict as a key and the value is incremented by 1
4. During each pass, I check if the seen[num] dict value is greater than n/2 as this would prove the num is the majority element of the array
5. If seen[num] is greater than n / 2, return num, else, continue iterating through nums.

## Complexity
- Time: O(n)
- Space: O(m)

## Notes
Discovered the Boyer-Moore Majority Voting Algorithm solving this problem.
