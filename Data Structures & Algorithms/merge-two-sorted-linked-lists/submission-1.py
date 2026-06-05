# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        cur = head = list1 if list1.val < list2.val else list2
        cur1 = list1.next if head == list1 else list1
        cur2 = list2.next if head == list2 else list2

        while cur1 and cur2:
            print('cur1 val',cur1.val)
            print('cur2 val',cur2.val)
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        
        while cur1:
            cur.next = cur1
            cur = cur.next
            cur1 = cur1.next
        while cur2:
            print(cur.val)
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next
        
        return head






        