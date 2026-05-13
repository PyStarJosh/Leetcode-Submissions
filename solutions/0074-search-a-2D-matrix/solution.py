class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True

            elif matrix[mid][0] < target and matrix[mid][-1] > target: 
                inner_start, inner_end = 0, len(matrix[mid]) - 1

                while inner_start <= inner_end:
                    inner_mid = inner_start + (inner_end - inner_start) // 2

                    if matrix[mid][inner_mid] == target:
                        return True
                    elif matrix[mid][inner_mid] > target:
                        inner_end = inner_mid - 1
                    else:
                        inner_start = inner_mid + 1
                
                return False

            elif matrix[mid][0] > target:
                end = mid - 1

            else:
                start = mid + 1

        return False
