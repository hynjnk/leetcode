class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        if isNegative:
            x = -x
        
        result = 0
        while x > 0:
            result *= 10
            x, m = divmod(x, 10)
            result += m
        
        if isNegative:
            if result > 1<<31:
                return 0
            else:
                return -result
        else:
            if result >= 1<<31:
                return 0
            else:
                return result

if __name__ == '__main__':
    print(Solution().reverse(321))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse(0))
    print(Solution().reverse(123123213000012322287))
