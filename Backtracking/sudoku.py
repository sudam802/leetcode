class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
# checking in rows
 
        for row in board :
            seen=set()
            for w in row:
                if w!=".":
                    if(w not in seen):
                        seen.add(w)
                    else:
                        return False
# checking for  columns
        for col in range(9):
            seen=set()

            for row in  range(9):
                d=board[row][col]
                if d!=".":
                    if(d not in seen):
                        seen.add(d)
                    else:
                        return False
 # checking for box
        for i in range(3):
            for j in range(3):
                seen = set()
                for x in range(i * 3, i * 3 + 3):
                    for y in range(j * 3, j * 3 + 3):
                        d=board[x][y]
                        if d != ".":
                            if d not in seen:
                                seen.add(d)
                            else:
                                return False

        return True

        
