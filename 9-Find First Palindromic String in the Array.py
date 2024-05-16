class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        for word in words:
            if word == word[::-1]:
                return word

        return ""

sample1 = ["abc", "car", "ada", "racecar", "cool"]
sample2 = ["notapalindrome", "racecar"]
sample3 = ["def", "ghi"]

s = Solution()
res = s.firstPalindrome(sample3)

print(res)