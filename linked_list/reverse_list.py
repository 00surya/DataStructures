from typing import Counter
from linked_list import LinkedList2 as ln_d

arr = [1,2,3,4,5,6]

lst = ln_d()
for i in arr:
    lst.push(i)

lst.print_list()


def pr(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev

    return head

hd = reverse_list(lst.head)
pr(hd)
