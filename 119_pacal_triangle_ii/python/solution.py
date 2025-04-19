from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for row_idx in range(2, rowIndex + 1):
            prev_value = row[0]
            for col_idx in range(1, row_idx):
                prev_value, row[col_idx] = row[col_idx], row[col_idx] + prev_value
        return row

print(Solution().getRow(3))
