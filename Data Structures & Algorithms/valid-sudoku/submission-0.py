class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use defaultdict(set) to easily track which numbers we've seen
        # Each will store digits that have already appeared in:
        # - A given row
        # - A given column
        # - A given 3×3 square
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3) identifies which 3x3 box we’re in
         # Iterate through every cell in the 9×9 Sudoku board
        for r in range(9):  # Loop over each row
            for c in range(9): # Loop over each column
            # Skip empty cells (represented by ".")
                if board[r][c] == ".":
                    continue
                # Check if the current number (board[r][c]) already exists
                # in the same row, same column, or same 3×3 square.
                # If it does, that violates Sudoku rules, so the board is invalid.
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # Otherwise, record this number in the corresponding sets:
                # - The row it’s in
                # - The column it’s in
                # - The 3×3 square it’s in
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True