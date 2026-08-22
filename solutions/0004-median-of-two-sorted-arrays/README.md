# Intuition
- To find the median of both arrays, we must find the value(s) that will reside within the middle of the two arrays. We can accomplish this by using binary search to partition the arrays as if they were conjoined
- To ensure correct partitioning, we must check that the end of the left partition values are less than or equal to the values at the beginning of the right partition.
- Once we have the correct partition, we can simply return the compute the median based on the whether the total number of elements is even or odd
- To further optimize, our algorithm, we can only utilize binary search on the smaller array granting us the time complexity of O(log(min(n, m)))

# Approach
1. Initialize total conjoined array size and halfway point
```python3 []
total = len(a) + len(b)
half = total // 2
```
2. Set one array variable to the smaller array of the two provided arrays 
```python3 []
if len(b) < len(a):
  a, b = b, a

left = 0
right = len(a) - 1
```
3. While True, calculate the ending index of array 1 and 2 portion of the left partition
```python3 []
while True:
  a_idx = (left + right) // 2
  b_idx = half - a_idx - 2
```
4. Initialize the 2 last elements in the left partition and the 2 starting values in the right partition, include edge cases check
```python3 []
a_left = a[a_idx] if a_idx >= 0 else float("-infinity")
a_right = a[a_idx + 1] if a_idx + 1 < len(a) else float("infinity")
b_left = b[b_idx] if b_idx >= 0 else float("-infinity")
b_right = b[b_idx + 1] if b_idx + 1 < len(b) else float("infinity")
```
5. If partitioning is correct, calculate and return the median
```python3 []
if a_left <= b_right and b_left <= a_right:
  if total % 2 == 0:
    return (max(a_left, b_left) + min(a_right, b_right)) / 2
  else:
    return min(a_right, b_right)
```
6. If the smaller arrays left partition endpoint is greater than the larger arrays right partition starting value, reduce the range of search for the smaller array partition
```python3 []
elif a_left > b_right:
  right = a_idx - 1
```
7. Else, if the left partition endpoint for the larger array is greater than the smaller array starting right partition element
```python3 []
else:
  left = a_idx + 1
```

# Complexity
- Time complexity:
O(log(min(n, m)))
- Space complexity:
O(1)

# Code
```python3 []
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        total = len(a) + len(b)
        half = total // 2
        
        if len(b) < len(a):
            a, b = b, a
        
        left = 0
        right = len(a) - 1

        while True:
            a_idx = (left + right) // 2
            b_idx = half - a_idx - 2

            a_left = a[a_idx] if a_idx >= 0 else float("-infinity")
            a_right = a[a_idx + 1] if a_idx + 1 < len(a) else float("infinity")
            b_left = b[b_idx] if b_idx >= 0 else float("-infinity")
            b_right = b[b_idx + 1] if b_idx + 1 < len(b) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                else:
                    return min(a_right, b_right)
            elif a_left > b_right:
                right = a_idx - 1
            else:
                left = a_idx + 1
```
