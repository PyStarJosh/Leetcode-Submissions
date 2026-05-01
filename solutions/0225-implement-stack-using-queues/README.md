# 0225. Implement Stack Using Queues

**Difficulty:** Easy

**Topics:** Stacks, Queues

**Link:** https://leetcode.com/problems/implement-stack-using-queues/

## Approach
I noticed the only difference between a stack and a queue is their push operations, so I concluded if I can rotating the queue after each push, it would be simply the same as pushing to the top of a stack. I decided the best way to 
implement this hypothesis was to utilize the queue's 'pop()' funciton to remove and return the leading value. I would take the returned value and append it to the back of the queue for 'n-1' iterations to ensure the last pushed item remains
at index 0 of the queue. This reodering essentially allows me to pop, peek, and push to the front of the queue.

## Complexity
- Time:
  - push: O(n)
  - pop: O(1)
  - top: O(1)
  - empty: O(1)

- Space: O(n)

## Notes
I struggled with this problem initially as I couldn't find a way to rotate the values keeping the latest push item at the front of the queue. I looked at the discussion tab for hints and saw someone mention 'use q2 to store the elements temp
orarily when pushing and popping. This sparked the idea behind my approach. My mistake when doing this problem was not writing out each function call result steo-by-step as this would have allowed me to better identify a reversal pattern.
