# 0560. Subarray Sum Equals K

**Difficulty:** Medium

**Topics:** Arrays, HashMaps, Prefix Sums

**Link:** https://leetcode.com/problems/subarray-sum-equals-k/

## Problem
This problem asks to return to return the amount of sub-arrays in the given array whose cunulative sums equals to k.

## Algo
My strategy to solve this problem evolved around the two sum leetcode problem as
they have similar problem characteristics. However, this question ask you to find a sub-array instead of one element, so I decided to use a HashMap to keep track of the cumulative sum at the end of each loop. This allows me to
subtract k from the current sum and check the HashMap for the difference and increment count by how many times this difference has been found in previous sub-arrays. This works as the running total being tracked in the HashMap
are just the cumulative sum of previous sub-arrays, so I can find how many sub-arrays in the array equal difference, I can figure out how many times I can set this current sum equal to k by removing a section of the previous sub-arrays.

1. Initialize cur_sum and count to 0
2. Initialize prefix_sums HashMap loaded with 0:1 as the first key-value pair to cover the case where cur_sum == k
3. Traverse nums
4. Add num to cur_num each iteration
5. Subtrack k from cur_sum each iteration to get the difference
6. Increment count by prefix_sum[diff] or by 0
7. Add a key:value pair for prefix_sums[cur_sum] or increment it by 1
8. After the int array have been traversed, return count

## Complexity
- Time: O(n) - Traversing nums
- Space: O(n) - prefix_sums HashMap possess N key-value pairs

## Notes
None
