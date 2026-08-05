class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        ans = []

        for pos, mph in cars:
            time_taken = (target - pos) / mph

            if not ans or time_taken > ans[-1]:
                ans.append(time_taken)

        return len(ans)
