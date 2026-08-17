class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            mid: int = left + (right - left) // 2

            if nums[mid] == target:
                return mid
                
            elif target > nums[mid]:
                if nums[left] > nums[mid] and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1

            elif target < nums[mid]:
                if nums[right] < nums[mid] and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
