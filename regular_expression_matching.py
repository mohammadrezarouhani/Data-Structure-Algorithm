# https://leetcode.com/problems/regular-expression-matching/description/


# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".


# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


import pdb
import string


class Solution:
    def isMatch(self, st: str, pt: str) -> bool:
        index = -1
        p_index = -1

        while index < len(st)-1:
            index += 1
            p_index += 1

            if p_index < len(pt):
                next_p = pt[p_index]
            else:
                return False

            if p_index+1 < len(pt) and pt[p_index+1] == '*':
                temp = index

                if st[index] != next_p and pt[index] != '.':
                    index -= 1
                    p_index += 1
                    continue

                while True:
                    if index+1 < len(st) and st[temp] == st[index+1]:
                        index += 1
                    elif pt[temp] == '.' and index+1 < len(st):
                        if p_index+2 < len(pt) and pt[p_index+2] in string.ascii_letters and pt[p_index+1] not in st:
                            return False
                        else:
                            index += 1
                            p_index += 1
                    else:
                        p_index += 1
                        break

            elif next_p in string.ascii_letters:
                if next_p != st[index]:
                    return False

            elif next_p == '.':
                if not st[index] in string.ascii_letters:
                    return False

        return True


s = Solution()

print(s.isMatch("aaa", 'aaaa'))
