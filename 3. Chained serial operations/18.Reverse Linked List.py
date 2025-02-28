#題目要求將一個單向鏈表反轉。反轉操作需要將鏈表中每一個節點的
#  next 指針指向前一個節點，最終返回反轉後的鏈表頭

from typing import Optional

# 定義單向鏈結串列的節點結構
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點的數值
        self.next = next  # 下一個節點的指標

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head  # 初始化兩個指標，prev 指向前一個節點，curr 指向當前節點
        
        # 當 curr 不為 None 時，繼續反轉
        while curr:
            temp = curr.next  # 儲存當前節點的下一個節點，防止丟失鏈結
            curr.next = prev  # 反轉當前節點的指向，讓它指向前一個節點
            prev = curr  # prev 向前移動，成為當前節點
            curr = temp  # curr 向前移動，繼續下一輪
        
        # 當循環結束後，prev 會指向新的頭節點（即原本的鏈結串列的尾部）
        return prev  # 返回反轉後的鏈結串列頭節點

##題目重點
# 遍歷每個節點，逐一反轉每個節點的 next 指向    