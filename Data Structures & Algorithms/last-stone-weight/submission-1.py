import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        hp = []
        for stone in stones:
            hp.append(-1 * stone)
        
        heapq.heapify(hp)

        while len(hp) > 1:
            weight_1 = (heapq.heappop(hp) * (-1))
            weight_2 = (heapq.heappop(hp) * (-1))
            # print('weight_1', weight_1)
            # print('weight_2', weight_2)

            new_val = weight_1 - weight_2 if weight_1 > weight_2 else weight_1 < weight_2
            #print('diff:', new_val)

            if new_val != 0:
                val = -1 * new_val
                heapq.heappush(hp, val)
        
        return hp[0] * (-1) if len(hp) > 0 else 0

            
        