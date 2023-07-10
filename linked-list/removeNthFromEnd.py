class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        # Create a dummy node and connect it to the head
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers
        fast = slow = dummy

        # Move the fast pointer to the nth node from the beginning
        for _ in range(n):
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next
