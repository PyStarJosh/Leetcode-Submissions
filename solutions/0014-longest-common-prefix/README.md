# 0014. Longest Common Prefix

**Difficulty:** Easy

**Topics:** Array

**Link:** https://leetcode.com/problems/longest-common-prefix/

## Approach
This problem asks to return a string of the longest commmon prefix that is shared by strings within an array. I realized that each string must have share the prefix, so we could utilize the first element as a base to compare the remanining
strings to in determining the prefix. However, I must handle the edge case when there is an element with less characters than the first element. I handled this edge case by finding the shortest string and using it's index as the end index for my loop. For the engine of this solution, I simply compared the same index of each string in the array to find the longest prefix. Once the loop came across an index where every element didn't share the same char, the loop would be broken and it would return result

## Complexity
- Time: O(n * m)
- Space: O(m)

## Notes
I found that determining the optimal time complexity before implementing the solution gives you insight into what algos would work for your solution. In addition, it helps manage the expectations of your result.
