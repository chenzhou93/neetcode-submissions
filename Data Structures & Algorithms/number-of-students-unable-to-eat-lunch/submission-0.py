from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dq = deque(students)
        pos = cnt = 0

        while len(dq) != cnt:
            val = dq.popleft()
            if val == sandwiches[pos]:
                pos += 1
                cnt = 0
            else:
                dq.append(val)
                cnt += 1
        
        return len(dq)
        

