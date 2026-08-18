# Intuition
- The sorted array is rotated at a pivot index between 0 and N - 1 meaning the array is still sorted, but finding the range that target exists in requires more condition checks.
- In addition, the array contains duplicates which prevent automatic determining of sorted range within the array, so we must linearly search for a unique value to determine our sorted range.
- We can find this range while eliminating half the array per iteration by searching for the range that breaks the ascending order via a mid, left and right pointer.
  - If the element at index left is smaller or equal to element at index middle, we can check if the target exist within this range. If so, we tighten our range from left to mid - 1.
  - Else, we check if the target exist within the range from element at index mid and element at index right. If, so we tighten our range to mid + 1 to right.
- This problem is the standard binary search problem, but with unknown ranges due to the rotations and duplicate values via non-descending order.

# Approach
1. 1. Initialize your left and right pointer
```python3 []
left: int = 0
right: int = len(nums) - 1
```
2. Set while loop to terminate when one element is present in the array.
```python3 []
while left <= right:
```
3. Calculate mid pointer value
```python3 []
mid: int = left + (right - left) // 2 # this overflow preventing form is not needed in python
```
4. Check if the nums[mid] == target
```python3 []
if nums[mid] == target:
  return True
```
5. Check if elements at mid and left are duplicate values
```python3 []
if nums[mid] == nums[left]:
  left += 1
  continue
```
5. Check the ranges in the array around the mid pointer followed by checking if the target fits in that range
```python3 []
if nums[left] <= nums[mid]:
  if nums[left] <= target < nums[mid]:
    right = mid - 1
  else:
    left = mid + 1
else:
  if nums[mid] < target <= nums[right]:
    left = mid + 1
  else:
    right = mid - 1
```
6. If the return statement has not been activated and the last element is compared to target, return -1
```python3 []
return False
```

# Complexity
- Time complexity:
O(n) worst case, O(log n) avg case -> Time complexity degrades as the number of duplicates increase in the array.

- Space complexity:
O(1)

# Code
```python3 []
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            mid: int = left + (right - left) // 2

            if nums[mid] == target:
                return True
            if nums[mid] == nums[left]:
                left += 1
                continue

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid - 1
        
        return False
```
