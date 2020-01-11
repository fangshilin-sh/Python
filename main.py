class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    
    def isValidSudoku(self, board):
        row = [range(1,10) for i in range(9)]
        column = [range(1,10) for i in range(9)]
        square = [range(1,10) for i in range(9)]
        
        blank_list = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    # remove one element from the list
                    value = int(board[i][j])
                    row[i].remove(value)
                    column[j].remove(value)
                    square[(i / 3) * 3 + (j / 3)].remove(value)
                else:
                    blank_list.append((i,j))
        print 'row'
        for i in row:
            print i
        print 'column'
        for j in column:
            print j
        print 'square'
        for i in square:
            print i
        return self.find_answer(board, row, column, square, blank_list)
        
    def find_answer(self, board, row, column, square, blank_list):
        # check if it is correct or not
        if (len(blank_list) == 0):
            return True
        for i in row:
            if len(i) == 0:
                return False
        for i in column:
            if len(i) == 0:
                return False
        for i in square:
            if len(i) == 0:
                return False
        
        #pick the first one
        x, y = blank_list[0]
        blank_list.remove((x,y))
        #pick the value
        for i in range(1,10):
            if i in row[x] and i in column[y] and i in square[(x / 3) * 3 + (y / 3)]:
                value = i
                row[x].remove(value)
                column[y].remove(value)
                square[(x / 3) * 3 + (y / 3)].remove(value)
                if (find_answer(board, row, column, square, blank_list)):
                    return True
                    
                row[x].append(value)
                column[y].append(value)
                square[(x / 3) * 3 + (y / 3)].append(value)
        return False
        
                

        
        
        
def main():
    s = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    x = Solution()
    print x.isValidSudoku(s)
main()
