import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_list = []
        for point in points:
            distance = math.sqrt((point[1] ** 2 + point[0] ** 2))
            distance = -1 * distance
            distance_list.append(distance)
            
        tpl = zip(distance_list, points)

        cnt = 0
        h = []
        for distance, point in tpl:
            item = (distance, point)
            if cnt < k:
                heapq.heappush(h, item)
                cnt += 1
            else:
                # print('h[0]', h[0])
                # print('item', item)
                if h[0] < item:
                    heapq.heapreplace(h, item)

        res = []
        for distance, point in h:
            res.append(point)
        #print(res)

        return res

        