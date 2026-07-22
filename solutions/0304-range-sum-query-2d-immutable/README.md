# 304. Range Sum Query 2D

**Difficulty:** Medium

**Topics:** Prefix Sums, Matrix (2D Arrays)

**Link:** https://leetcode.com/problems/range-sum-query-2d-immutable/

## Problem Statement
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:
NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

You must design an algorithm where sumRegion works on O(1) time complexity.

## Algo
My strategy for solving this problem was to implement a prefix sums algo on the two dimensional array and use inclusive-exclusive principle to only get the sums of the targeted region.

1. Create a prefixSum grid with one extra row and column of zeros (padding).
2. prefixSum[r][c] means: sum of everything from (0,0) to (r-1, c-1).
3. Fill it in: prefixSum[r+1][c+1] = matrix[r][c] + above + left - overlap.
4. "Above" = prefixSum[r][c+1], "left" = prefixSum[r+1][c], "overlap" = prefixSum[r][c].
5. Overlap is subtracted because above and left both include it once.
6. To query a rectangle (row1,col1) to (row2,col2), start with the full sum prefixSum[row2+1][col2+1].
7. Subtract everything above the region: prefixSum[row1][col2+1].
8. Subtract everything left of the region: prefixSum[row2+1][col1].
9. Add back prefixSum[row1][col1] since it was subtracted twice.
10. Result: rectangle sum in O(1) time.

## Complexity
- Time: O(1) for each query
- Space: O(m * n)
