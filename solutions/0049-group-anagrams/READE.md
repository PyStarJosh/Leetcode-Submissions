# 0049. Group Anagrams

**Difficulty:** Medium

**Topics:** HashMap

**Link:** https://leetcode.com/problems/group-anagrams/

## Approach

1. Initalize Default Dictionary to hold Grouped Anagrams
2. Iterate through each string in strs
3. Initialize a Char Count Array of 26 elements, one for each alphabetical character
4. Count the Frequency of Each Char in the String using ASCII values to determine the correct index to increment by 1
5. Convert the Char Count Array into a tuple and set the tuple as a key for the defaultdict
6. Append the current String to it's respective Char Count tuple key
7. Return the Grouped Anagrams

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## Notes
ord() converts a char into it's ASCII value
Dictionaries can't use an array as a key since it is not a hashable data structure
