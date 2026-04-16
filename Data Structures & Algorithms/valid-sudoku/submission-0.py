from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize defaultdicts where the key is the index (row/col) 
        # or the (r//3, c//3) tuple for the square, and the value is a set 
        # to store seen digits.
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # Key is (r // 3, c // 3)

        # Iterate through the 9x9 board
        for r in range(9):
            for c in range(9):
                cell_value = board[r][c]

                # We only process cells that contain a digit (not '.')
                if cell_value == ".":
                    continue

                # --- 1. Check Row Constraint ---
                # Check if the digit is already in the current row's set.
                if cell_value in rows[r]:
                    return False
                # Add the digit to the current row's set.
                rows[r].add(cell_value)
                
                # --- 2. Check Column Constraint ---
                # Check if the digit is already in the current column's set.
                if cell_value in cols[c]:
                    return False
                # Add the digit to the current column's set.
                cols[c].add(cell_value)

                # --- 3. Check 3x3 Sub-box Constraint ---
                # Calculate the unique key for the 3x3 sub-box (0-8)
                # Integer division (// 3) groups the indices:
                # (0, 0), (0, 1), (0, 2) maps to key (0, 0)
                # (3, 3), (3, 4), (3, 5) maps to key (1, 1)
                square_key = (r // 3, c // 3)
                
                # Check if the digit is already in the current square's set.
                if cell_value in squares[square_key]:
                    return False
                # Add the digit to the current square's set.
                squares[square_key].add(cell_value)

        # If the loop completes without finding any violations, the board is valid.
        return True