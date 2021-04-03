class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        ten_digit_list = []
        while x:
            x, m = divmod(x, 10)
            ten_digit_list.append(m)
        for i in range(len(ten_digit_list)//2 + 1):
            if ten_digit_list[i] != ten_digit_list[-i-1]:
                return False
        return True

    def isPalindromeIntToString(self, x: int) -> bool:
        s = str(x)
        print(s)
        for i in range(len(s)//2 + 1):
            # print(f'i: {i} {s[i]} {s[-i-1]}')
            if s[i] != s[-i-1]:
                return False
        return True
        

if __name__ == '__main__':
    print(Solution().isPalindrome(0))
    print(Solution().isPalindrome(10101))
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(1221))
    print(Solution().isPalindrome(10))
    print(Solution().isPalindrome(122))
    print(Solution().isPalindrome(-12))