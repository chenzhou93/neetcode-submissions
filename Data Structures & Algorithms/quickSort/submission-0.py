# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quick_sort(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        
        left = s

        for i in range(s, e):
            if pairs[i].key < pairs[e].key:
                tmp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = tmp
                left += 1
        
        tmp = pairs[e]
        pairs[e] = pairs[left]
        pairs[left] = tmp

        self.quick_sort(pairs, s, left - 1)
        self.quick_sort(pairs, left+1, e)

        return pairs


    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs) - 1
        return self.quick_sort(pairs, s, e)
        