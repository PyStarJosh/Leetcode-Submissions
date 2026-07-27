class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a-1]:
                a += 1
                continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b-1]:
                    b += 1
                    continue

                diff = target - nums[a] - nums[b]
                left = b + 1
                right = n - 1

                while left < right:
                    total = nums[left] + nums[right]
                    if total == diff:
                        res.append([nums[a], nums[b], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        
                        while right > left and nums[right] == nums[right+1]:
                            right -= 1

                    elif total > diff:
                        right -= 1

                    else:
                        left += 1    

        return res
