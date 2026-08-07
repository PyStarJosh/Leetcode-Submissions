# 0071. Simplify Path

**Difficulty:** Medium

**Topics:** Stack, String

**Link:** https://leetcode.com/problems/simplify-path

## Problem Statement
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

## Algo
My strategy for solving this problem was to split the string by "/" regex giving me an array of each directory name. I would iterate through the array of directories and check the directory string value. If it was "..", I would pop from the stack only
if the stack is not empty. If it was "" or "", I would do nothing, else, I would put the directory onto the stack

1. Initialize directory array by splitting given string by "/"
2. Iterate through the directory array, checking the string values
3. If string value is "..", pop() from the stack if and only if the stack is populated
4. Else if the string value is "" or ".", do nothing
5. Else, pop() the directory onto the stack
6. Return the joined stack split with "/" as the delimiter with a leading "/"
   
## Complexity
- Time: O(n) -> 3 traversals of size n arrays
- Space: O(n) -> 2 initialization of n sized data structures
