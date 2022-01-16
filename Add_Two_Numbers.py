# -*- coding: utf-8 -*-
"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit.

Add the two numbers and return the sum as a linked list.


Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
    
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

---


Runtime: o(n)
    
Runtime: 111 ms
Memory Usage: 14.1 MB <-- top 2% in Leet-code
    
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def extract_number(single_p):
    
    sum_of_pointer = 0
    factor = 0
    
    while(single_p.next):
        sum_of_pointer += single_p.val * 10 ** factor
        factor += 1
        single_p = single_p.next
        
    return sum_of_pointer


def addTwoNumbers(l1, l2):
 
    sum_of_pointers = ListNode()
    current_number = sum_of_pointers
    transfer_value = 0
    factor = 0
    
    while(l1 or l2):
        
        step_value = 0
        
        if l1:
            step_value += l1.val
            l1 = l1.next
        
        if l2:
            step_value += l2.val
            l2 = l2.next
        
        step_value += transfer_value
                  
        current_number.val = int((step_value % 10))
        current_number.next = ListNode()
        last_value = current_number
        current_number = current_number.next
        
        transfer_value = int((step_value - step_value % 10)/10)
        factor += 1
    
    if transfer_value > 0:
        current_number.val = transfer_value
    else:
        last_value.next = None
    
    return sum_of_pointers 
        

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


print(extract_number(addTwoNumbers(l1, l2)))
