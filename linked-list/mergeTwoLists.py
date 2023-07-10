
# Define ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # Create a dummy node and initialize pointers
        dummy = ListNode(0)
        current = dummy
        p1 = l1
        p2 = l2

        # Traverse both lists and merge
        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        # Append remaining nodes
        if p1:
            current.next = p1
        else:
            current.next = p2

        return dummy.next



# Define ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Remove the 2nd node from the end
solution = Solution()
result = solution.removeNthFromEnd(head, 2)

# Expected Output: 1 -> 2 -> 3 -> 5 -> None
while result:
    print(result.val, end=" ")
    result = result.next
print()
