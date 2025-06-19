def checkmate(boaed: str):
    board = board,strip(),split('\n')
    slice = len(board)

    # Check if board is a square
    for row in board:
        if len(row) != size:
            print("Error")
            return
        
# Find King
king_pos = None
for i in range(size):
    for j in range(len(board[i])):
        if board[i][j] == 'K':
            king_pos = (1, j)
            break
    if king_pos:
        break

if not king_pos:
    print("Error")
    return

def in_bounds(x, y):
    return 0 <= x < size and 0 <= y < len(board[x])

def is_pawn_attacking():
    x, y = king_pos
    for dx, dy in [(-1, -1), (-1, 1)]:
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny) and board[nx][ny] == 'P':
            return True
    return False

def is_bishop_attacking():
    x, y = king_pos
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, -1)]:
        nx, ny = x + dx, y + dy
        while in_bounds(nx, ny):
            plece = board