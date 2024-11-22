
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0

        for i1, h1 in enumerate(heights):
            if h1 > max_area:
                max_area = h1

            for j1 in range(i1 + 1, len(heights)):
                new_rect = heights[i1 : j1 + 1]
                new_area = min(new_rect) * len(new_rect)

                if new_area > max_area:
                    max_area = new_area

        return max_area


s = Solution()
answer = s.largestRectangleArea([2,4])

print(answer == 4)
