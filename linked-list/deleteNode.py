# Define ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        # Copy the value of the next node to the current node
        node.val = node.next.val

        # Skip the next node by updating the next pointer
        node.next = node.next.next



# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Given the node with value 3 to be deleted
node_to_delete = head.next.next

# Delete the node
solution = Solution()
solution.deleteNode(node_to_delete)

# Traverse the modified linked list
# Expected Output: 1 -> 2 -> 4 -> 5 -> None
current = head
while current:
    print(current.val, end="->")
    current = current.next
print(None)
