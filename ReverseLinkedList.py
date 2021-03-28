def reverseList(self, head: ListNode) -> ListNode:
    # begin with temporary node
    cur = ListNode(-1)

    # continue while list exists
    while head is not None:
        # create temp and make temp the new cur
        temp = ListNode(-1)
        cur.val = head.val
        temp.next = cur
        cur = temp
        head = head.next


    return cur.next