# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head) :
        dummy=ListNode()
        dummy.next=head
        p=dummy

        while p.next and p.next.next:
            if p.next.val==p.next.next.val:
               duplicate_val = p.next.val
               while p.next and p.next.val == duplicate_val:
                    p.next = p.next.next
            else:
                p=p.next
        return dummy.next




# Create a sorted linked list with duplicate nodes: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> None
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

# Remove nodes with duplicate numbers
solution = Solution()
result = solution.deleteDuplicates(head)

# Traverse the modified linked list
# Expected Output: 2 -> 4 -> 5 -> None
current = result
while current:
    print(current.val, end=" ")
    current = current.next
print()
