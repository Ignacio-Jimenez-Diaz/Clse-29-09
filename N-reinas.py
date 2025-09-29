#ITERATIVO
board = array of size n (initially -1, indicating no queen)
col = 0
row_positions = array to store row for each column

while col >= 0:
    found = false
    for row from 0 to n-1:
        if is_safe(row, col, board):
            board[col] = row
            found = true
            break
    if found:
        if col == n-1:
            // Solution found, record it
            solutions.add(copy of board)
            col -= 1  // Backtrack to find more solutions
        else:
            col += 1  // Move to next column
    else:
        board[col] = -1  // Reset current column
        col -= 1  // Backtrack to previous column
        if col >= 0:
            board[col] += 1  // Try next row in previous column

function is_safe(row, col, board):
    for i from 0 to col-1:
        if board[i] == row or
           abs(board[i] - row) == abs(i - col):
            return false
    return true