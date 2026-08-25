# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        i = 1
        node = head

        before = after = None
        prev = cur = None

        leftNode = None

        while node:
            if i == (left - 1):
                before = node
            elif i == left:
                leftNode = node
                cur = node
            elif i == right:
                after = node.next
                break

            node = node.next
            i += 1

        # reverse
        while cur != after:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        if before:
            before.next = prev
        else:
            head = prev

        leftNode.next = after

        return head

        