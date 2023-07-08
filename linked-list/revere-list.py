class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None





"""Iterative Approach:

In the iterative approach, we will iterate through the linked list
and reverse the next pointers of each node to point to the
previous node instead of the next node.     """

class Solution1:
    def reverseList(self, head):
        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node
    
"""
Recursive Approach:

In the recursive approach, we will use a recursive function
 to reverse the linked list. The idea is to reverse the rest of the 
 list after the current node and then update the next pointer of 
the current node and return the new head of the reversed list.

"""
class Solution2:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head


# Test example 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution1()
reversed_head = solution.reverseList(head)
# Output: [5, 4, 3, 2, 1]
while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next
print()

# Test example 2
head = ListNode(1)
head.next = ListNode(2)

solution = Solution2()
reversed_head = solution.reverseList(head)
# Output: [2, 1]
while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next

# Test example 3
head = None

solution = Solution1()
reversed_head = solution.reverseList(head)
# Output: []
print(reversed_head)

