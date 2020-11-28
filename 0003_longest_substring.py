#! /usr/bin/env python3


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if length of a string is lower than 2,
        # longest substring of the string is itself.
        if len(s) < 2:
            return len(s)
        sub_len = 1
        start = 0
        for i in range(1, len(s)):
            new_start = s[start:i].find(s[i]) + start + 1
            #print("start", start, "new_start", new_start, "i", i, end=" ")
            if new_start > start:
                start = new_start
            else:
                new_len = i + 1 - start
                if new_len > sub_len:
                    sub_len = new_len
            #print("sub_len", sub_len)
        return sub_len

if __name__ == '__main__':
    s = "abcabcbb"
    s = "abcabcbbasdfghjklbnmvcbbabc"
    #s = "ab"
    print(Solution().lengthOfLongestSubstring(s))
