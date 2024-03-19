from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0]*nums[1])-(nums[-1]*nums[-2])
        




if __name__=="__main__":
    s=Solution()
    res=s.maxProductDifference([4,2,5,9,7,4,8])
    print(res)