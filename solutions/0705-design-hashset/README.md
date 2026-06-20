# 0705. Design HashSet

**Difficulty:** Easy

**Topics:** HashSet

**Link:** https://leetcode.com/problems/design-hashset/

## Approach
1. Initialize the number of buckets
2. Initialize each bucket in an matrix called buckets to hold hashed data
3. Implement a rudimentary hashing function
4. Access the correct bucket based on the hashed key and add it to the bucket, if it is not already in it
5. Access the correct bucket based on the hashed key and remove it from the bucket, if present in the bucket
6. Access the correct bucket based on the hashed key and return a boolean value based on whether the bucket contains the hashed key

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
None
