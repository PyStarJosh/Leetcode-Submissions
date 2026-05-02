class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index in range(len(nums)):
            val = nums[index]
            diff = target - val

            if diff in seen:
                return [seen[diff], index]

            seen[val] = index
