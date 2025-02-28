# 給定兩個已排序的鏈表，合併為一個新的已排序鏈表，並返回合併後的結果


from typing import Optional      # 引入Optional（因為下面的程式碼有用到型別註解）

# 創建鏈結串列的基本結構
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:        
            return list2
        if not list2:       
            return list1

        # 比較兩個鏈結串列的當前節點，選擇較小的作為新的起點
        if list1.val < list2.val:
            #合併 list1 的下一個節點與 list2，直到處理完所有節點
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            #接著合併剩下的部分
            list2.next = self.mergeTwoLists(list1, list2.next)       
            return list2

##題目重點
#1. 理解鏈結串列的操作，如何透過 node.next 來指向下一個節點
#2. 遞迴：每次遞迴選擇較小的元素並將其加入合併結果中，然後繼續處理剩下的部分
#3. 在class內部的函式中，我們需要使用 self 來引用當前物件的屬性和函式(第21、25行)

        



        