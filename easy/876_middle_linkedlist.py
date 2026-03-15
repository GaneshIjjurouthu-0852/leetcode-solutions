class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def build(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next
def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
head = build([1, 2, 3, 4, 5])
res = middleNode(head)
print(res.val) 