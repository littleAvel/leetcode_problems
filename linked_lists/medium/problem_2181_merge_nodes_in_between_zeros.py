# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TODO: review this problem later
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next
        sum_node = node

        while sum_node:
            sum_val = 0

            while sum_node.val != 0:
                sum_val += sum_node.val
                sum_node = sum_node.next

            node.val = sum_val
            sum_node = sum_node.next

            node.next = sum_node
            node = node.next
        return head.next