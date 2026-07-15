from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                curr = 1
                seq = num + 1

                while seq in num_set:
                    curr += 1
                    seq += 1

                res = max(res, curr)

        return res
