'''

'''
def isValid(board, row, col, num):
    # validate num in comparison to row, col, and 3 * 3 sub-grid
    for x in range(9):
        if board[row][x] == num:
            return False
        if board[x][col] == num:
            return False
        if board[(row//3)*3 + x//3][(col//3)*3 + x%3] == num:
            return False
    return True

def solveSudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                for num in range(1,10):
                    if isValid(board,row, col, num):
                        board[row][col] = str(num)
                        if solveSudoku(board):
                            return True
                        else:
                            board[row][col] = "."
                    return False
    return True



def main():

    # Test case 1
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']]


    print(solveSudoku(board))  
    # expected output:  5 3 4 6 7 8 9 1 2 
    #                   6 7 2 1 9 5 3 4 8 
    #                   1 9 8 3 4 2 5 6 7 
    #                   8 5 9 7 6 1 4 2 3 
    #                   4 2 6 8 5 3 7 9 1 
    #                   7 1 3 9 2 4 8 5 6 
    #                   9 6 1 5 3 7 2 8 4 
    #                   2 8 7 4 1 9 6 3 5 
    #                   3 4 5 2 8 6 1 7 9
    print(board)

    # Test case 2
    board = [['8', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '3', '6', '.', '.', '.', '.', '.'],
        ['.', '7', '.', '.', '9', '.', '2', '.', '.'],
        ['.', '5', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '.', '4', '5', '7', '.', '.'],
        ['.', '.', '.', '1', '.', '.', '.', '3', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '6', '8'],
        ['.', '.', '8', '5', '.', '.', '.', '1', '.'],
        ['.', '9', '.', '.', '.', '.', '4', '.', '.']]
    print(solveSudoku(board))
    # expected output:  8 1 2 7 5 3 6 4 9 
    #                   9 4 3 6 8 2 1 7 5 
    #                   6 7 5 4 9 1 2 8 3 
    #                   1 5 4 2 3 7 8 9 6 
    #                   3 6 9 8 4 5 7 2 1 
    #                   2 8 7 1 6 9 5 3 4 
    #                   5 2 1 9 7 4 3 6 8 
    #                   4 3 8 5 2 6 9 1 7 
    #                   7 9 6 3 1 8 4 5 2
    print(board)      

main()
