class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        total = len(a) + len(b)
        half = total // 2
        
        if len(b) < len(a):
            a, b = b, a
        
        left = 0
        right = len(a) - 1

        while True:
            a_idx = (left + right) // 2
            b_idx = half - a_idx - 2

            a_left = a[a_idx] if a_idx >= 0 else float("-infinity")
            a_right = a[a_idx + 1] if a_idx + 1 < len(a) else float("infinity")
            b_left = b[b_idx] if b_idx >= 0 else float("-infinity")
            b_right = b[b_idx + 1] if b_idx + 1 < len(b) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                else:
                    return min(a_right, b_right)
            elif a_left > b_right:
                right = a_idx - 1
            else:
                left = a_idx + 1
