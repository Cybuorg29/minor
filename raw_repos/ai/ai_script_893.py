class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initialize current, previous and 
        # next pointers 
        curr1 = l1
        curr2 = l2
        head = None
        prev = None
        
        carry = 0
        while curr1 != None or curr2 != None or carry != 0:
            val1 = 0
            if curr1 != None:
                val1 = curr1.val
                curr1 = curr1.next
            
            val2 = 0
            if curr2 != None:
                val2 = curr2.val
                curr2 = curr2.next
                
            val = val1 + val2 + carry
            carry = val // 10
            temp = ListNode(val%10)

            if prev == None:
                head = temp
            else:
                prev.next = temp
            
            prev = temp

        return head