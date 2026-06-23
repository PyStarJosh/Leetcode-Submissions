class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        middle = len(nums) // 2
        left_arr = nums[:middle]
        right_arr = nums[middle:]

        left_arr = self.sortArray(left_arr)
        right_arr = self.sortArray(right_arr)

        return self._merge(left_arr, right_arr, arr=nums)
        


    def _merge(self, left_arr: List[int], right_arr: List[int], arr: List[int]) -> List[int]:
        '''Merges sub-arrays after sorting them.'''
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

        return arr
