# 1768. Valid Palindrome

**Difficulty:** Easy

**Topics:** Two Pointer

**Link:** https://leetcode.com/problems/merge-strings-alternately/

## Approach
This problem asks you to return a string with it's characters being the alternately appended characters from word1 and word2.
I decided to initialize my res variable as a list as it's more efficient to add to a list since it's a mutable data structure
in comparison to a string which must be overwritten each time due to it's immutable nature. Next, I initalized a while loop
to iterate as variable 'i' was less than word1's and word2's length allowing res to append all of the alternating characters.
This leaves the remaining characters of the larger string, so we simply used the python string splicing due to it's indexing tolerance
appending 'word[i:]' to the end of 'res'. Finally, we conver the array back into a string using the ''.join(array) method which
takes the elements of an iterable and combines them into a string.


## Complexity
- Time: O(n + m)
- Space: O(n + m)

## Notes
I learned about python's .join() method and the indexing tolerance of splicing in python which prevents you from raising a indexerror.
