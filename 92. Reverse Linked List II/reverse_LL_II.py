class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head

    left_prev = dummy
    curr = head
    i = 1

    while i < left:
        left_prev = curr
        curr = curr.next
        i += 1

    left_node = curr
    prev = None

    while i <= right:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1

    left_prev.next = prev       # connect before
    left_node.next = curr       # connect after

    return dummy.next