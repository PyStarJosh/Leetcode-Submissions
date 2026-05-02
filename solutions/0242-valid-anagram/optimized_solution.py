from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        '''
        Counter creates a dict of an iterable such as a list or string where the keys are the iterable's
        elements and the values are the amount of time the elements appear in the iterable

        Example: i1 = 'car' i2 = 'rat'
        Counter(i1) = {
            'c': 1,
            'a': 1,
            'r': 1,
        }

        Counter(i2) = {
            'r': 1,
            'a': 1,
            't': 1,
        }

        This allows for us to utilize the value equivalence operator to check if the dicts' have the same
        keys and values
        '''
