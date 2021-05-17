from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.bulidParenthesis('', n, n)

    def canOpen(self, remain_open: int) -> bool:
        return remain_open > 0

    def canClose(self, remain_open: int, remain_close: int) -> bool:
        return remain_open < remain_close

    def bulidParenthesis(
        self, s: str, remain_open: int, remain_close: int
    ) -> List[str]:
        if remain_open == 0 and remain_close == 0:
            return [s]

        result = []
        if self.canOpen(remain_open):
            result += self.bulidParenthesis(
                s + '(', remain_open - 1, remain_close
            )
        if self.canClose(remain_open, remain_close):
            result += self.bulidParenthesis(
                s + ')', remain_open, remain_close - 1
            )
        return result
