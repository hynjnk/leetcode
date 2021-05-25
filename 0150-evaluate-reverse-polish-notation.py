import unittest
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token = tokens.pop()
        if '0' <= token[-1] and token[-1] <= '9':
            return int(token)

        right = self.evalRPN(tokens)
        left = self.evalRPN(tokens)

        print(f'{left} {token} {right}')
        if token == '+':
            return left + right
        elif token == '-':
            return left - right
        elif token == '*':
            return left * right
        else:  # token == '/'
            # division between two integers should truncate toward zero
            if (left < 0) ^ (right < 0):
                return -(-left // right)
            return left // right