# 0128. Longest Consecutive Sequence

**Difficulty:** Medium

**Topics:** Hashset, Arrays

**Link:** https://leetcode.com/problems/longest-consecutive-sequence/

## Approach
This problem asks you to return the length of the longest consecutive sequence of numbers in the given array.
My stategy was to use a HashSet to capture the unique elements within the arry and iterate through the elements that were the beginning of a sequence to find the next sequential number.
If the number existed in the hashset increment the current sequence length variable and return the max from curr and res to return the correct length. 

1. Initalize HashSet to hold unique elements, set res to 0
2. Iterate through each num that does not start a sequence
3. While the next sequential value of the current num is in the HashSet, increment current and the sequential value by 1 iteratively.
4. Once the while loop terminates, assign the max between res and curr to res variable
5. When the for loop is complete, return res which houses the largest consecutive sequence in the array

## Complexity
- Time: O(n)
- Space: O(u) - unique elements in HashSet

## Notes
At first, I started the count for every value that had the next sequential value in the HashSet. However, this was
slow with a time complexity of O(n^2) in the worst case scenario. This solution was inefficient, becuase it created a count for each sub-section of an larger
sequence resulting in unnecessary operations. I improved my algo by checking if the current num was apart of a larger sequence before counting.
