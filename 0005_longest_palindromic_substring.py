class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return s
        maxlen = 0
        now = 0, 0

        # check odd length palindrome substring
        for left in range(len(s)):
            right = left
            while self.isPalindrome(s, left - 1, right + 1):
                left -=1
                right += 1
            if right - left + 1 > maxlen:
                now = left, right
                maxlen = right - left + 1

        # check even length palindrome substring
        for left in range(len(s) - 1):
            if self.isPalindrome(s, left, left + 1):
                right = left + 1
                while self.isPalindrome(s, left - 1, right + 1):
                    left -=1
                    right += 1
                if right - left + 1 > maxlen:
                    now = left, right
                    maxlen = right - left + 1
            
        return s[now[0]:now[1] + 1]

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        if left < 0:
            return False
        if right >= len(s):
            return False
        return s[left] == s[right]
        

if __name__ == '__main__':
    # s = "babad"
    # s = "cbbd"
    # s = "a"
    # s = "ac"
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(Solution().longestPalindrome(s))