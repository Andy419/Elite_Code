def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ''' basic linked list, get to a certain vertex and continue on
        '''
        
        # set dummy and actual movement
        dummy = final = ListNode(-1)
        
        final.next = list1
        
        # go to a
        for _ in range(a):
            final = final.next
        
        temp = final.next
        final.next = list2
        
        # go past list 2
        while final.next is not None:
            final = final.next
        
        for _ in range(b-a+1):
            temp = temp.next
        
        
        # add rest of list 1
        final.next = temp
        return dummy.next