# 0217. Contains Duplicate

**Difficulty:** Easy

**Topics:** HashSet

**Link:** https://leetcode.com/problems/contains-duplicate/

## Approach
This problem give you an int array and asks you to return True, if the array contains duplicate values and False, if it contains no duplicate elements. I decided the best approach for this problem would be a python HashSet as it has
o(1) search time complexity. Then, I iterated through nums and used a if statement to check if the value already exists in my set, if it does the function returns True and if it does not then the function adds the element to the set. Once
I iterated through n finding no duplicates my function simply returns False.

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
I initially thought of the brute force approach using 2 nested for loops, but I knew that would be O(n^2), so I decided to pursue another algorithm. Then, I thought of sorting the array and simply checking if two sequential index contained
the same value, but due to python's built in sorting function being O(n log n) this algorithm was not optimal. Finally, I thought of my current solution using a HashMap, but after reviewing other solutions, I noticed HashSet was the better data
structure to use in this solution.
