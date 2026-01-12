# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None

    slow = head
    fast = head.next

    while fast:
        if slow.val == fast.val:
            slow.next = fast.next
            fast = fast.next
        else:
            slow = slow.next
            fast = fast.next

    return head

"""
def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    current = head

    while current is not None and current.next is not None:
        if current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next

    return head
"""