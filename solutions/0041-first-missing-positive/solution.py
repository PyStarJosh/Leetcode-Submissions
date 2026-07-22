class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for idx in range(n):
            while (1 <= nums[idx] <= n) and (nums[idx] != nums[nums[idx] - 1]):
                val = nums[idx]
                nums[idx], nums[val - 1] = nums[val - 1], nums[idx]
        
        for idx in range(n):
            if nums[idx] != idx + 1:
                return idx + 1

        return n + 1
