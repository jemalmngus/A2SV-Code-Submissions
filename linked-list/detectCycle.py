# Define ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        p1 = head
        p2 = head
        has_cycle = False

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                has_cycle = True
                break

        if not has_cycle:
            return None

        p1 = head

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1

# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (back to node 3)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next

# Test the detectCycle function
solution = Solution()
cycle_start = solution.detectCycle(head)

if cycle_start:
    print("Cycle detected! Starting node of the cycle:", cycle_start.val)
else:
    print("No cycle detected.")
