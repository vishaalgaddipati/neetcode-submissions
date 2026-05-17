class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # track with hashmap where key is row num and val is hashset of 1-9
       rowDupes = defaultdict(set)
       colDupes = defaultdict(set)
       boxDupes = defaultdict(set) 

       for i in range(len(board)):
        for j in range(len(board[i])):
            # skip blank cells
            if board[i][j] == '.':
                continue
            if board[i][j] in rowDupes[i]:
                return False
            elif board[i][j] in colDupes[j]:
                return False
            # this computation numbers the board boxes 0-8 and fits i, j indices into them
            # using integer division. so index (8,3) becomes 7 which is the bottom middle box
            elif board[i][j] in boxDupes[(i//3)*3+(j//3)]:
                return False
            else:
                rowDupes[i].add(board[i][j])
                colDupes[j].add(board[i][j])
                boxDupes[(i//3)*3+(j//3)].add(board[i][j])
       return True