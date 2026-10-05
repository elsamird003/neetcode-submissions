#include <vector>

class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        // Bitmasks for tracking numbers seen in each row, col, and 3x3 box
        std::vector<int> rows(9, 0);
        std::vector<int> cols(9, 0);
        std::vector<int> boxes(9, 0);

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                char ch = board[r][c];
                
                // Skip empty cells
                if (ch == '.') continue;

                int val = ch - '1'; // Map '1'-'9' to bits 0-8
                int mask = 1 << val;
                int box_idx = (r / 3) * 3 + (c / 3);

                // Check for duplicates across row, column, or sub-box
                if ((rows[r] & mask) || (cols[c] & mask) || (boxes[box_idx] & mask)) {
                    return false;
                }

                // Record the digit in row, column, and sub-box
                rows[r] |= mask;
                cols[c] |= mask;
                boxes[box_idx] |= mask;
            }
        }

        return true;
    }
};