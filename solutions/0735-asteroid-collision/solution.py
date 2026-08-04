class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteroid in asteroids:
            if asteroid > 0:
                res.append(asteroid)
            else:
                if not res:
                    res.append(asteroid)
                else:
                    while True:
                        if res[-1] < 0:
                            res.append(asteroid)
                            break

                        top = res[-1]
                        diff = top - abs(asteroid)

                        if diff > 0:
                            break
                        elif diff == 0:
                            res.pop()
                            break
                        else:
                            res.pop()

                            if not res:
                                res.append(asteroid)
                                break
        
        return res
