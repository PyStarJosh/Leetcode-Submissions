# 0347. Top K Frequent Elements

**Difficulty:** Medium

**Topics:** Array, Hashing, Sorting

**Link:** https://leetcode.com/problems/top-k-frequent-elements/

## Approach
This problem asks for the top K most frequent elements in a integer array. My initial solution to this problem used the 'Counter' class and appended it's content into an array converting it into a metrix that I used a lambda key to get the max
element based on it's value at index 1. We'll do this kth times to get our answer. However, this answer was slow with a time complexity of O(n * k) and O(n^2) in worst case scenarios.

So, I came upon my second solution which is utilizing bucket sort to store all numbers in an array by their indices allowing me to easilt access the top k elements in O(n) time. 
    1. Initiate a Counter object with the integer array as the param
    2. Initiate the matrix, buckets which will hold the integers at the index of their frequency in the original array
    3. Create a result array
    3. Iterate through the Counter object for it's key and freq to append the key to 'buckets' matrix at index freq
    4. Iterate through buckets backwards coming across the highest freq indexes first.
    5. Iterate through bucket[freq] to get the corresponding integer and append it to the result array.
    6. Once the length of the result array equals k, return result.

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
I learned how to get the max of a metrix based on the nested list second value using a lambda key.
