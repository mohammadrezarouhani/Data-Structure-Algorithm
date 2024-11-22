from typing import List
from pprint import pprint

def twoSum( nums: List[int], target: int) -> List[int]:
    hashmap={nums[i]:i for i in range(0,len(nums))}

    for i in range(0,len(nums)):
        complement=target-nums[i]
        if complement in hashmap and hashmap[complement]!=i:
            return [i,hashmap[complement]]

 q
pprint(twoSum([2,7,11,15],9))