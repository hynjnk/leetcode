class Solution:
    def __init__(self):
        self.encoded_set = set(str(i) for i in range(1, 27))

    def numDecodings(self, s: str) -> int:
        '''
        Solve using buttom-up approch to DP.
        time complexity O(n)
        space complexity O(1)
        '''
        prev = 1
        cur = 1 if s[0] in self.encoded_set else 0
        for i in range(1, len(s)):
            new = 0
            if s[i] in self.encoded_set:
                new += cur
            if s[i-1:i+1] in self.encoded_set:
                new += prev

            prev, cur = cur, new
            if prev == 0 and cur == 0:
                return 0

        return cur
