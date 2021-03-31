def oddEvenList(self, head: ListNode) -> ListNode:
        # Create two linked lists
        dummy1 = odd = ListNode(-1)
        dummy2 = even = ListNode(-1)
        
        # iterate through until no longer possible
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            if head.next is None:
                break
            elif head.next.next is None:
                odd.next = head.next
                break
            else:
                head = head.next.next
        
        # get rid of first dummy elements and return
        odd.next = dummy2.next
        return dummy1.next