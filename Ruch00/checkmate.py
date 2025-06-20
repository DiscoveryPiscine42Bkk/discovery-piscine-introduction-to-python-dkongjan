def is_king_in_check(*rows):
    board = [list(row) for row in rows]
    n = len(board)

    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail") 
        return

    ki, kj = king_pos

    def on_board(x, y):
        return 0 <= x < n and 0 <= y < n

    def check_linear(dx, dy, threats):
        x, y = ki + dx, kj + dy
        while on_board(x, y):
            if board[x][y] == '.':
                x += dx
                y += dy
                continue
            return board[x][y] in threats
        return False

    def check_knight():
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]
        for dx, dy in moves:
            x, y = ki + dx, kj + dy
            if on_board(x, y) and board[x][y] == 'N':
                return True
        return False

    def check_pawn():
        for dx, dy in [(-1, -1), (-1, 1)]:
            x, y = ki + dx, kj + dy
            if on_board(x, y) and board[x][y] == 'P':
                return True
        return False

    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if check_linear(dx, dy, ['R', 'Q']):
            print("Success")
            return

    
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if check_linear(dx, dy, ['B', 'Q']):
            print("Success")
            return

    
    if check_knight():
        print("Success")
        return

    
    if check_pawn():
        print("Success")
        return

    print("Fail")
    
is_king_in_check(
    ".......",
    "...Q...",
    ".......",
    "...K...",
    ".......",
    ".......",
    "......."
)
