import re


class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = re.compile('^ *([+-]{0,1})([0-9]+)')
        result = pattern.match(s)

        if not result:
            return 0
        
        i = int(result.group(2))
        if result.group(1) == '-':
            i = -i
            if i < -(1<<31):
                i = -(1<<31)
        elif i > ((1<<31) - 1):
            i = (1<<31) - 1
        
        return i
    

if __name__ == '__main__':
    print(Solution().myAtoi(''))
    print(Solution().myAtoi('aaasdf 339 '))
    print(Solution().myAtoi('-39aa'))
    print(Solution().myAtoi('42'))
    print(Solution().myAtoi('2147483648'))
    print(Solution().myAtoi('-2147483648'))
    print(Solution().myAtoi('-2147483649'))