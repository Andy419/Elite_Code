def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        
        return False