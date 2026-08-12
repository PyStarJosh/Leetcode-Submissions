class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][0] > height:
                curr_height, popped_idx = stack.pop()
                w = idx - popped_idx
                max_area = max(max_area, curr_height * w)
                start = popped_idx
            stack.append((height, start))

        while stack:
            height, idx = stack.pop()
            w = n - idx
            max_area = max(max_area, height * w)
        
        return max_area
