def solve_sudoku(puzzle):
    """
    Solve a Sudoku puzzle using backtracking.
    
    Parameters:
    puzzle: a list of lists representing the Sudoku puzzle. The puzzle is assumed to be a 9x9 grid with empty cells represented by 0.
    
    Returns:
    A list of lists representing the solved Sudoku puzzle.
    """
    
    # Find the next empty cell in the puzzle
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                # Try filling in the empty cell with a number from 1 to 9
                for k in range(1, 10):
                    # Check if the number is valid for the current cell
                    if is_valid(puzzle, i, j, k):
                        # If it is, fill in the cell and try solving the rest of the puzzle
                        puzzle[i][j] = k
                        if solve_sudoku(puzzle):
                            return puzzle
                # If none of the numbers work, backtrack
                puzzle[i][j] = 0
                return False
    # If there are no more empty cells, the puzzle is solved
    return True

def is_valid(puzzle, row, col, num):
    """
    Check if a given number is valid for a given cell in the puzzle.
    
    Parameters:
    puzzle: a list of lists representing the Sudoku puzzle.
    row: the row index of the cell to check.
    col: the column index of the cell to check.
    num: the number to check.
    
    Returns:
    True if the number is valid for the cell, False otherwise.
    """
    
    # Check if the number appears in the same row or column
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False
    
    # Check if the number appears in the same 3x3 block
    block_row = row // 3
    block_col = col // 3
    for i in range(3):
        for j in range(3):
            if puzzle[block_row * 3 + i][block_col * 3 + j] == num:
                return False
    
    # If the number does not appear in the same row, column, or block, it is valid
    return True


puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
]

solve_sudoku(puzzle)