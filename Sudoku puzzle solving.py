def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid(board, row, col, num):
    
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_cell = find_empty(board)

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True  
            
            board[row][col] = 0

    return False 

sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Puzzle:")
print_board(sudoku_board)
print("\nSolving...\n")

if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists.")

