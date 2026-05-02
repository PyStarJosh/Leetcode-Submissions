# 0242. Valid Anagram

**Difficulty:** Easy

**Topics:** HashMap

**Link:** https://leetcode.com/problems/valid-anagram/

## Approach
This problems calls for you to return a boolean value that's based on whether the 2 provided strings are anagrams of one another. I started my method off by returning false if the lengths of the first string and second string were different.
Them I decided to use a Python 'defaultdict(int)' to collect the string chars as keys and their occurrence in the string as the value. I implemented this by iterating through one string, saving the element as a key, and incrementing its 
value by 1 each time it's passed. Then, I would iterate through the second string to decrement the dict values by 1 to if both strings have the same number of occurrences for this value and the length check at the beginning guarantee's the strings equal.
At the end, I would iterate through my defaultdict values, return false if any value did not equal 0, or return true.

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
My solution worked and met the fastest complexity, but it inefficiently written as I missed multiple quick checks to reduce runtime. In addition, I learned that Python has a built in collection subclass called Counter that builds the data str
ucture I constructed in my code in a more idiomatic manner with the same time complexity. I also learned that sorting the two strings and comparing their values
is the most space efficient solution. 
