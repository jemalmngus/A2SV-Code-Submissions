# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
       
        p1=p2=head
     
        while p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
            
        return p1    

# Test example
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
result = solution.middleNode(head)
# Expected Output: [3, 4, 5]
while result:
    print(result.val, end=" ")
    result = result.next
print()
                                              