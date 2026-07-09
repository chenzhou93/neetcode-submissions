import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tpl = []
        for point in points:
            distance = (point[1] ** 2 + point[0] ** 2)
            distance = -1 * distance
            tpl.append((distance, point))
            

        h = []
        for item in tpl:
            if len(h) < k:
                heapq.heappush(h, item)
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

        