class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def build(values):
    dummy=ListNode(0)
    curr=dummy
    for v in values:
        curr.next=ListNode(v)
        curr=curr.next
    return dummy.next
def cycle_exist(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False
head=build([3,2,0,-4,2])
#Manual wire the cycle
last=head
while last.next:
    last=last.next
last.next=head.next

res=cycle_exist(head)
print(res)

        