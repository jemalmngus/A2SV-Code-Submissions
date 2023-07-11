# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        p1=p2=head

        while p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                return True
        return False
    

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (back to node 3)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next

# Test the hasCycle function
solution = Solution()
has_cycle = solution.hasCycle(head)

if has_cycle:
    print("Cycle detected!")
else:
    print("No cycle detected.")
