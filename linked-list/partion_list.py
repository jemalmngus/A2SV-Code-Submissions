class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        Problem: Partition List

        Given the head of a linked list and a value x, partition it such that all nodes less than x
        come before nodes greater than or equal to x. You should preserve the original relative order
        of the nodes in each of the two partitions.

        Solution:
        - We create two separate lists: one for nodes less than x and one for nodes greater than or equal to x.
        - We iterate through the original list and add each node to the respective list based on the value.
        - After processing all the nodes, we link the end of the smaller list to the head of the greater list.
        - Finally, we return the head of the combined list.

        :param head: Head of the linked list
        :param x: Value to partition the list
        :return: Head of the partitioned list
        """
        p1 = ListNode(None)
        p2 = ListNode(None)
        p1_head = p1
        p2_head = p2

        while head:
            if head.val < x:
                p1.next = ListNode(head.val)
                p1 = p1.next
            else:
                p2.next = ListNode(head.val)
                p2 = p2.next

            head = head.next

        p1.next = p2_head.next

        return p1_head.next
# Test example
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

solution = Solution()
result = solution.partition(head, 3)
# Expected Output: [1, 2, 2, 4, 3, 5]
while result:
    print(result.val, end=" ")
    result = result.next
print()
