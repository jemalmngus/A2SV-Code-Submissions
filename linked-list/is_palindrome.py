class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        
class Solution:
    def isPalindrome(self, head):
        # Helper function to reverse a linked list
        def reverseList(node):
            prev = None
            curr = node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Base case: If the list is empty or has only one node, it is a palindrome
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list starting from the slow pointer
        second_half = reverseList(slow)

        # Compare the reversed second half with the first half
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next

        return True
# Test example
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

solution = Solution()
result = solution.isPalindrome(head)
# Expected Output: True
print(result)
