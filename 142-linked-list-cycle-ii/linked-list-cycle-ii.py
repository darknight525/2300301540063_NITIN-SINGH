# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = fast = head

        

        # Step 1: detect cycle

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

            

            if slow == fast:

                break

        else:

            return None   

        

        # Step 2: find start

        slow = head

        

        while slow != fast:

            slow = slow.next

            fast = fast.next

        

        return slow

        
       