# medium
# Given a string s, return the longest
# palindromic
# substring
# in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"


# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters.



class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = s[0]

        for i in range(len(s)):
            if s[i] in s[0:i]:
                max = self.check(s, i, max)

        return max

    def check(self, s, i, max):

        for j in range(i):
            sub = s[j : i + 1]
            if sub == sub[::-1] and len(s[j : i + 1]) > len(max):
                max = s[j : i + 1]

        return max


s = Solution()

print(s.longestPalindrome("aba"))
