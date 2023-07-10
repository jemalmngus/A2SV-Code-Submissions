# Define ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head


# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reorder the linked list
solution = Solution()
result = solution.oddEvenList(head)

# Traverse the modified linked list
# Expected Output: 1 -> 3 -> 5 -> 2 -> 4 -> None
current = result
while current:
    print(current.val, end=" ")
    current = current.next
print()
