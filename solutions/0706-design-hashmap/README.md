# 0706. Desgin HashMap

**Difficulty:** Easy

**Topics:** HashMap, Array

**Link:** https://leetcode.com/problems/design-hashmap/

## Approach
This problem asks you to design a HashMap from scratch. 

1. First, I initialzied a preset number of buckets to store the nested list that would act as our mapping data structure.
2. I implemented a rudimentary _hash function to reduce the chance of collisions in my HashMap.
3. I created a helper _get_bucket method to reduce code verbosity.
4. I decided to employ a HashMap that utilizes closed addressing to take advantage of it's anti-clustering principles as opposed to open addressing with it's space benefits.
5. In my put method, I used python's enumerate() method to access the bucket's nested list index and keys to find the key and overwrite the value or append the new key-value pair to the end of the list.
6. In my get method, I iterated through the nested list in the bucket to access the passed key's value if it existed within the secondary array
7. I used enumerate in my remove method to find the correct key-value pair to pop from the secondary array

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
I learned the internal of hashmaps and terminology related to the data structure such as load factor, linear probbing, clustering, and open/closed addressing.
