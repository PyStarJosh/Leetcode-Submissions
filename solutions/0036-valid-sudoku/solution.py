from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        sub_box = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == '.':
                    continue
                
                box_num = (r // 3) * 3 + (c // 3)

                if any(element in s for s in (row[r], column[c], sub_box[box_num])):
                    return False
                else:
                    row[r].add(element)
                    column[c].add(element)
                    sub_box[box_num].add(element)     

        return True
