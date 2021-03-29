def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # get length of A
        fakeA = headA
        counta = 0
        while fakeA != None:
            counta += 1
            fakeA = fakeA.next
        
        # get length of B
        fakeB = headB
        countb = 0
        while fakeB != None:
            countb += 1
            fakeB = fakeB.next
        
        # make the two lists the same length
        while counta != countb:
            if counta > countb:
                headA = headA.next
                counta -= 1
            else:
                headB = headB.next
                countb -= 1
        
        # continue down the bigger list until the two lists are equal
        while headA and headB:
            if headA == headB:
                return headA
            if counta >= countb:
                headA = headA.next
                counta -= 1
            else:
                headB = headB.next
                countb -= 1
        
        # if the lists never equal each other, return None
        return None