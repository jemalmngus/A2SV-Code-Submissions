# Define ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

# Create a sorted linked list with duplicates: 1 -> 1 -> 2 -> 3 -> 3 -> None
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

# Remove duplicates from the linked list
solution = Solution()
result = solution.deleteDuplicates(head)

# Traverse the modified linked list
# Expected Output: 1 -> 2 -> 3 -> None
current = result
while current:
    print(current.val, end=" ")
    current = current.next
print()
