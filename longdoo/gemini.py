import sys

def is_king_in_check(board_rows):
    """
    Checks if the King on the chessboard is "in check" by any enemy piece.

    This function considers attacks from Pawns ('P'), Bishops ('B'), Rooks ('R'),
    and Queens ('Q'). The board can be of varying square sizes. All characters
    not representing a specific piece are treated as empty squares.

    Args:
        board_rows: A list of strings, where each string represents a row of the
                    chessboard. For example: ["...K....", "....P...", "........"]

    Prints:
        "Success" followed by a newline if the King is in check.
        "Fail" followed by a newline if the King is not in check.
        Error messages to standard error if the input is invalid or
        unexpected conditions are met (e.g., no King, multiple Kings,
        non-square board).
    """
    # Validate input: Ensure board_rows is not empty
    if not board_rows:
        print("Error: Empty board provided.", file=sys.stderr)
        return

    # Convert the list of strings into a 2D list (matrix) for easier indexing.
    # Also, perform basic validation on row types.
    board = []
    for row_str in board_rows:
        if not isinstance(row_str, str):
            print("Error: All board rows must be strings.", file=sys.stderr)
            return
        board.append(list(row_str))

    board_size = len(board)

    # Validate board dimensions: Ensure it's a non-empty square board.
    if board_size == 0 or not all(len(row) == board_size for row in board):
        print("Error: Board is not square or has invalid dimensions.", file=sys.stderr)
        return

    king_pos = None
    king_count = 0

    # Find the King's position and count the number of Kings.
    for r in range(board_size):
        for c in range(board_size):
            if board[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    # Handle cases where no King or multiple Kings are found.
    if king_count == 0:
        print("Error: No King ('K') found on the board.", file=sys.stderr)
        return
    if king_count > 1:
        print("Error: Multiple Kings ('K') found on the board. Only one is allowed.", file=sys.stderr)
        return

    # Unpack King's row and column.
    king_r, king_c = king_pos

    # Helper function to check if a given row and column are within the board boundaries.
    def is_valid_position(r, c):
        return 0 <= r < board_size and 0 <= c < board_size

    # --- Check for attacks from Rooks ('R') and Queens ('Q') ---
    # These pieces attack horizontally and vertically.
    # Directions: (delta_row, delta_column) for Up, Down, Left, Right
    horizontal_vertical_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in horizontal_vertical_directions:
        current_r, current_c = king_r + dr, king_c + dc
        # Continue scanning in this direction as long as the position is valid.
        while is_valid_position(current_r, current_c):
            piece = board[current_r][current_c]
            if piece == 'R' or piece == 'Q':
                # King is in check if a Rook or Queen is found on this line of sight.
                print("Success")
                return
            elif piece != '.':
                # If a non-empty piece is found that is not a threatening piece,
                # it blocks the line of sight, so stop checking this direction.
                break
            # Move to the next square in the current direction.
            current_r += dr
            current_c += dc

    # --- Check for attacks from Bishops ('B') and Queens ('Q') ---
    # These pieces attack diagonally.
    # Directions: (delta_row, delta_column) for Up-Left, Up-Right, Down-Left, Down-Right
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        current_r, current_c = king_r + dr, king_c + dc
        # Continue scanning in this direction as long as the position is valid.
        while is_valid_position(current_r, current_c):
            piece = board[current_r][current_c]
            if piece == 'B' or piece == 'Q':
                # King is in check if a Bishop or Queen is found on this line of sight.
                print("Success")
                return
            elif piece != '.':
                # If a non-empty piece is found that is not a threatening piece,
                # it blocks the line of sight, so stop checking this direction.
                break
            # Move to the next square in the current direction.
            current_r += dr
            current_c += dc

    # --- Check for attacks from Pawns ('P') ---
    # For this exercise, Pawns are assumed to attack any adjacent diagonal square.
    pawn_attack_offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in pawn_attack_offsets:
        pawn_r, pawn_c = king_r + dr, king_c + dc
        # Check if the diagonal square is valid and contains a Pawn.
        if is_valid_position(pawn_r, pawn_c) and board[pawn_r][pawn_c] == 'P':
            print("Success")
            return

    # If the function reaches this point, no attacking piece was found.
    print("Fail")

# --- Example Usage to demonstrate Success and Fail ---
if __name__ == "__main__":
    print("--- Test Cases ---")

    # Test case 1: King in check by a Rook
    print("\nTest Case 1: King in check by a Rook (Expected: Success)")
    board1 = [
        "........",
        "........",
        "...K....",
        "....R...",
        "........",
        "........",
        "........",
        "........"
    ]
    is_king_in_check(board1)

    # Test case 2: King not in check (no attacking pieces)
    print("\nTest Case 2: King not in check (Expected: Fail)")
    board2 = [
        "........",
        "........",
        "....K...",
        "........",
        "........",
        "........",
        "........",
        "........"
    ]
    is_king_in_check(board2)

    # Test case 3: King in check by a Queen (diagonal)
    print("\nTest Case 3: King in check by a Queen (diagonal) (Expected: Success)")
    board3 = [
        "Q.......",
        "........",
        "..K.....",
        "........",
        "........",
        "........",
        "........",
        "........"
    ]
    is_king_in_check(board3)

    # Test case 4: King in check by a Bishop (blocked by another piece)
    # The Bishop is on the diagonal, but a pawn blocks the check.
    print("\nTest Case 4: King not in check (Bishop blocked) (Expected: Fail)")
    board4 = [
        "B.......",
        ".P......",
        "..K.....",
        "........",
        "........",
        "........",
        "........",
        "........"
    ]
    is_king_in_check(board4)

    # Test case 5: King in check by a Pawn
    print("\nTest Case 5: King in check by a Pawn (Expected: Success)")
    board5 = [
        "........",
        "........",
        "....K...",
        "...P....",
        "........",
        "........",
        "........",
        "........"
    ]
    is_king_in_check(board5)

    # Test case 6: Empty board (Expected: Error)
    print("\nTest Case 6: Empty board (Expected: Error)")
    is_king_in_check([])

    # Test case 7: Board with multiple Kings (Expected: Error)
    print("\nTest Case 7: Board with multiple Kings (Expected: Error)")
    board7 = [
        "K...K...",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........"
    ]
    is_king_in_check(board7)

    # Test case 8: Board with no King (Expected: Error)
    print("\nTest Case 8: Board with no King (Expected: Error)")
    board8 = [
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........"
    ]
    is_king_in_check(board8)

    # Test case 9: Non-square board (Expected: Error)
    print("\nTest Case 9: Non-square board (Expected: Error)")
    board9 = [
        "....",
        "....",
        "....K",
        "...."
    ]
    is_king_in_check(board9)