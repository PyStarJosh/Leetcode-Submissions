from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freqs = defaultdict(int)    
        self.stacks = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        curr_val = self.freqs[val]
        self.max_freq = max(self.max_freq, curr_val)
        self.stacks[curr_val].append(val)
        
    def pop(self) -> int:
        res = self.stacks[self.max_freq].pop()
        self.freqs[res] -= 1

        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
        
        return res
