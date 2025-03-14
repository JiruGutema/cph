# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if not head:
        #     return False
        # objects = set()
        # current = head
        # while current.next != None:
        #     if current not in objects:
        #         objects.add(current)
        #         current = current.next
        #     else:
        #         return True
                
        # return False

        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        




                
