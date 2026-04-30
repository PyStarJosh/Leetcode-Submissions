class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = (len(nums) - 1)

        while start_index <= end_index:
            midpoint_index = start_index + (end_index - start_index) // 2

            if target == nums[midpoint_index]:
                return midpoint_index

            elif target > nums[midpoint_index]:
                start_index = midpoint_index + 1
            
            else:
                end_index = midpoint_index - 1
        
        return -1
