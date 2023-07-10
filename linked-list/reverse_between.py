class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
class Solution:
 
    def reverseBetween(self, head,left: int, right: int) :
        if left == right:
            return head


        # Create a dummy node and connect it to the head
        dummy = ListNode(0)
        dummy.next = head

        # Find the node at position left - 1
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing the nodes between left and right
        curr = prev.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next

# Test example
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
result = solution.reverseBetween(head, 2, 4)
# Expected Output: [1, 4, 3, 2, 5]
while result:
    print(result.val, end=" ")
    result = result.next
print()
