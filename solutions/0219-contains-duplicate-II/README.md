# 219. Contains Duplicate II

**Difficulty:** Easy

**Topics:** Array, HashMap

**Link:** https://leetcode.com/problems/contains-duplicate-II/

## Approach
This problem ask you to return a boolean value for the condition that the given array has two duplicate
elements within k indices of each other in the array. My strategy involves using a hashmap to store the values of the
array and their respective index as the value. This allows me to take advantage of hashmap's O(1) lookup to determine if a duplicate exist within the array.
After a duplicate is discovered, I will simply get the absolute value of the difference of the two array elements indices.

1. Initialize HashMap(dict) to store num as key and its index within the nums array as the value
2. Enumerate through the nums array
3. If current num is not in HashMap or abs(left_idx - right_idx) is not <= k, add or orverwrite the num into the HashMap with its index as the value
4. If the current num is in the HashMap and abs(left_idx - right_idx) is <= k, return True
5. If the entire array is iterated thorugh without the True termination condition being met, return False as no duplicates
within in k indices of each other exist in the array.

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
