# zigzag-conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
        P     I    N    0,       6,        12,
        A   L S  I G    1,    5, 7,    11, 13
        Y A   H R       2, 4,    8, 10,
        P     I         3        9,

        numRows period
        1   1
        2   2
        3   4
        4   6
        5   8
        '''
        if numRows == 1:
            return s

        converted = ""
        for row in range(numRows):
            for i in range(row, len(s), 2*(numRows-1)):
                converted += s[i]
                offset = 2*(numRows-1-row)
                if row > 0 and offset > 0 and i + offset < len(s):
                    converted += s[i + offset]
        return converted
