class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteroid in asteroids:

            while res and asteroid < 0 < res[-1]:
                if -asteroid > res[-1]:
                    res.pop()
                    continue
                elif -asteroid == res[-1]:
                    res.pop()   
                break
            else:
                res.append(asteroid)

        return res
