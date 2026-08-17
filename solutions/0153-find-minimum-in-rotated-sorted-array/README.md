# Intuition
- This problem has a time constraint of O(log N) along with a sorted array, so I know binary search will be a good algorithm for solving this problem.
- The sorted array is rotated from 1 to N times meaning the array is still sorted, but the beginning element of the sorted array position is lost. However, we can find this by discovering the overlap from the largest element(end) in
the array to the smallest element in the array(start).
- We can find this overlap while eliminating half the array per iteration by searching for the range that breaks the ascending order via a mid, left and right pointer.
  - If the element at index mid is greater than the element art index right, we know the overlap must occur within mid + 1 to right index.
  - Else, we know the overlap must occur in left pointer to mid, this case includes the value at mid because we have not found a value smaller than it yet. We just confirmed the overlap was not to the right of this index in the array.
- We will tighten our range until both left and right pointer converge to the one value which will be the smallest value in the sorted array. At this point, we will return the left or right pointer.

# Approach
1. Initialize your left and right pointer
```python3 []
left: int = 0
right: int = len(nums) - 1
```
2. Set while loop to terminate when one element is present in the array.
```python3 []
while left < right:
```
3. Calculate mid pointer value
```python3 []
mid: int = left + (right - left) // 2 # this overflow preventing form is not needed in python
```
4. Create your if-else statement for the value at mid compared to the value at right
```python3 []
if nums[mid] < nums[right]:
  right = mid
else:
  left = mid + 1
```
5. Once your while loop terminates
```python3 []
return nums[left]
```

# Complexity
- Time complexity:
O(log N)

- Space complexity:
O(1)

# Code
```python3 []
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left < right:
            mid: int = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
```
