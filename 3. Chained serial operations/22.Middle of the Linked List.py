#給定一個單向鏈表，請找出其中間節點。如果有兩個中間節點，返回第二個中間節點

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  not head:
            return None
        
        slow = head
        fast = head
            #如果fast還能走兩步（因為fast一次走兩步）
        while fast and fast.next:
            # slow 每次走一步
            slow = slow.next
            # fast 每次走兩步
            fast = fast.next.next
        return slow    # 當 fast 到達鏈表末尾時，slow 即為中間節點
    
##題目重點
# 如果鏈表長度為偶數，slow 會停在第二個中間節點（題目要求）    
# 如果只希望回傳「中間的節點」而不是整個後半段鏈表的結構，可以把最後的地方改成
# return slow.val
        