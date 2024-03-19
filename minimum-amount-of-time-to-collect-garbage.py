class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        trucks=['M','P','G']
        pickup_time=0

        for g in garbage:
            pickup_time+=len(g)

        for tr in trucks:
            for i in range(len(garbage) - 1, -1, -1):
                if tr in garbage[i] and i != 0:
                    for j in range(i):
                        pickup_time+=travel[j]
                    break

        return pickup_time
