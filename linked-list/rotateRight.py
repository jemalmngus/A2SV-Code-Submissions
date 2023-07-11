# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        
        self.next = next
class Solution:
    def rotateRight(self, head,k):

        # Check for empty list or zero rotation
        if not head or k == 0:
            return head
        
        # Calculate the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Effective rotation amount
        k = k % length
        
        # No rotation needed
        if k == 0:
            return head
        
        # Connect the tail to the original head
        tail.next = head
        
        # Find the new head position
        steps = length - k
        new_tail = tail
        while steps > 0:
            new_tail = new_tail.next
            steps -= 1
        
        # Set the next pointer of the previous node to None
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head



# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Rotate the list to the right by 2 places
solution = Solution()
k = 2
rotated_list = solution.rotateRight(head, k)

# Print the rotated list
# Expected Output: 4 -> 5 -> 1 -> 2 -> 3
current = rotated_list
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

      
       