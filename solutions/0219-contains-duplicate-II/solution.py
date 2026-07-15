class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for idx, value in enumerate(nums):
            if value in seen and abs(idx - seen[value]) <= k:
                return True
            seen[value] = idx

        return False
