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
        start = 0
        end = 0
        match_result = []
        pt_list = self.process_patterns(pt)

        for index, pattern in enumerate(pt_list):
            s, e, f, count = self.matchPosition(start, pattern, st, pt)
            match_result.append((s, e, f, pattern, count))
            start = e

        count_sum = sum([res[4] for res in match_result])
        if count_sum < len(st):
            return False

        for index, res in enumerate(match_result):
            if not self.final_process(res, st):
                return False

        return True

    def pre_process(self, match_results): # doesnt work
        stars = []
        count_sum = 0
        star_flag = False

        reversed_match = match_results[::-1]
        for i, res in enumerate(reversed_match):
            pattern = res[3]
            if '*' not in pattern:
                for j, match in enumerate(reversed_match[i+1:]):
                    if pattern not in match[3]:
                        count_sum += match[4]
                    else:
                        star_flag = True
                        break

                if count_sum == 0 and star_flag == True:
                    reversed_match.pop(i)

                star_flag = False
                count_sum = 0

        pdb.set_trace()
        return reversed_match[::-1]

    def final_process(self, match_res, st):
        s, e, f, pattern, count = match_res

        if not f:
            return False

        return True

    def matchPosition(self, start, pattern, st, pt):
        s = start
        e = start
        flag = True
        count = 0

        if '*' in pattern:
            if pattern[0] == '.':
                for index, letter in enumerate(st[start:]):
                    if letter in string.ascii_letters:
                        e = index
                        count += 1
            else:
                for index, letter in enumerate(st[start:]):
                    if letter == pattern[0]:
                        e += 1
                        count += 1
                    else:
                        break

        elif pattern == '.':
            if st[start] in string.ascii_letters:
                flag = True
                count = 1
            else:
                count = 0
                flag = False
            e += 1

        elif pattern in string.ascii_letters:
            if start < len(st) and pattern == st[start]:
                flag = True
                count = 1
            else:
                count = 0
                flag = False
            e += 1

        return (s, e, flag, count)

    def process_patterns(self, pt):
        pattern_list = []
        postion = 0
        star_flag = []

        for index, pattern in enumerate(pt):
            if pattern in string.ascii_letters or pattern == '.':
                pattern_list.append(pattern)
                postion += 1
            elif pattern == '*':
                pattern_list[postion-1] += '*'


        return pattern_list


s = Solution()

print('true match:')
print(s.isMatch("aaa", 'aaaa'))
print(s.isMatch("aaaa", 'ab*a*aac*a'))
print(s.isMatch("aaa", 'a*a'))
print(s.isMatch("mississippi", 'mis*is*ip*.'))

print(s.isMatch("aaabbbbbbbbbbbbbbbb", 'aaab*'))
print(s.isMatch("aa", 'a*'))
print(s.isMatch("ab", '.*'))
print(s.isMatch("a", '.'))
print(s.isMatch("a", 'c*a'))
print(s.isMatch("aab", 'c*a*b'))

print('\nfalse match:')
print(s.isMatch("aa", 'a'))
