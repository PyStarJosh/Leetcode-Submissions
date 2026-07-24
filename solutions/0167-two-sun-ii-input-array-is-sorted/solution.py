class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, z = 0, len(numbers) - 1

        while a < z:
            total = numbers[a] + numbers[z]

            if total == target:
                return [a + 1, z + 1]
            elif total > target:
                z -= 1
            else:
                a += 1
