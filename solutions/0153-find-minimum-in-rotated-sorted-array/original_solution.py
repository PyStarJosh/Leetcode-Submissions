class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]

            mid: int = left + (right - left) // 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[right]:
                left = mid 
            else:
                right = mid
