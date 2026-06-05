# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        cur = head
        next = cur.next
        
        while next:
            
            if cur == head:
                cur.next = None

            tmp = next.next
            next.next = cur
            
            cur = next
            next = tmp
        
        head = cur

        return head

            
            





            



        