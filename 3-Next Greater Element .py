class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums_idx = {n: i for i, n in enumerate(nums1)}
        result = [-1] * len(nums1)
        st = [] 

        for r in range(len(nums2)):
            cur = nums2[r]

            while st and cur > st[-1]:
                val = st.pop()
                pointer = nums_idx[val]
                result[pointer] = cur

            if cur in nums_idx:
                st.append(cur)

        return result


s = Solution()

print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
