class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        start, end = 0, rows * columns - 1
        while start <= end:
            mid = start + (end - start) // 2
            mid_row, mid_col = divmod(mid, columns)

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return False

  '''
  This method converts the matrix into a flat array and utilizes the divmod() method to get the corresponding coordinates as 'mid // columns' returns a quotient of the row index and a remainder of the column index to the mid index element. This allows improved readability compared to my original solution as it makes the code more
  succinct. I saw this solution from 'vanamsen' on LeetCode solutions.
  '''
