def partition(self, head: ListNode, x: int) -> ListNode:
        ''' Easy problem with easy solution.
            bascially just two linked lists and combine them in the end
        '''
        
        
        
        after = dummya = ListNode(-1)
        before = dummyb = ListNode(-1)
        
        while head is not None:
            if head.val < x:
                before.next = head
                before = before.next
            
            if head.val >= x:
                after.next = head
                after = after.next
             
            head = head.next

        after.next = None
        dummya = dummya.next
        before.next = dummya
        
        return dummyb.next