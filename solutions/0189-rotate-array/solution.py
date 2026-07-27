class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return

        def rev(left: int, right: int) -> list[int]:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)
