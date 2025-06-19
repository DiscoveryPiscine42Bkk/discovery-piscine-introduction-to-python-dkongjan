def checkmate(board_str: str):
    board = [list(row) for row in board_str.strip().split('\n')]
    size = len(board)

    # Check if board is a square
    for row in board:
        if len(row) != size:
            print("Error: Board is not square")
            return

    # Find King
    king_pos = None
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error: King not found")
        return

    # Check for attacks
    if (
        is_pawn_attacking(board, king_pos, size) or
        is_bishop_attacking(board, king_pos, size) or
        is_rook_attacking(board, king_pos, size)
    ):
        print("Success")
    else:
        print("Fail")

def in_bounds(x, y, board, size):
    return 0 <= x < size and 0 <= y < len(board[x])

def is_pawn_attacking(board, king_pos, size):
    x, y = king_pos
    for dx, dy in [(-1, -1), (-1, 1)]:
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny, board, size) and board[nx][ny] == 'P':
            return True
    return False

def is_bishop_attacking(board, king_pos, size):
    x, y = king_pos
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy
        while in_bounds(nx, ny, board, size):
            piece = board[nx][ny]
            if piece == '.':
                nx += dx
                ny += dy
            elif piece == 'B' or piece == 'Q':
                return True
            else:
                break
    return False

def is_rook_attacking(board, king_pos, size):
    x, y = king_pos
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        while in_bounds(nx, ny, board, size):
            piece = board[nx][ny]
            if piece == '.':
                nx += dx
                ny += dy
            elif piece == 'R' or piece == 'Q':
                return True
            else:
                break
    return False

if __name__ == "__main__":
    board = """
.......
.......
....K..
....P..
.......
.......
......."""
    checkmate(board)