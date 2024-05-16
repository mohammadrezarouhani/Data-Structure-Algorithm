class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        vote = 0
        for num in nums:
            if vote == 0:
                candidate = num
                vote = 1
            else:
                vote += 1 if candidate == num else -1

        return candidate


sample1 = [3, 2, 3]
sample2 = [2, 2, 1, 1, 1, 2, 2]

s = Solution()
res = s.majorityElement(sample1)

print(res)
