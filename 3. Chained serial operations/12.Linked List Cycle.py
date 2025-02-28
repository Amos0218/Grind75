# 給定一個單向鏈結串列，判斷它是否有環（cycle）

from typing import Optional 

##雙指針法（效率較高）
class ListNode:
    def __init__(self, x):
        self.val = x            # 節點的值
        self.next = None        # 指向下一個節點的指針，預設為 None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 如果鏈結串列是空的，直接返回 False
        if not head:
            return False
        
        # 初始化 slow 和 fast 指針，都指向頭節點
        slow = head
        fast = head
        
        # 當 fast 仍然能移動兩步時，繼續迴圈
        while fast and fast.next:
            # slow 每次走一步
            slow = slow.next
            # fast 每次走兩步
            fast = fast.next.next
            
            # 如果 slow 和 fast 相遇，表示有循環
            if slow == fast:
                return True
        
        # 如果 fast 走到結尾，沒有循環
        return False


##哈希表解法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 用一個集合來記錄已經遍歷過的節點，會自動幫我們過濾掉重複的節點
        visited = set()
        
        #當 head（當前節點）不為 None 時，遍歷鏈結串列
        while head:          
            # 如果當前節點已經在集合中，說明有循環
            if head in visited:
                return True
            # 將當前節點加入集合
            visited.add(head)
            # 移動到下一個節點
            head = head.next
        
        # 如果遍歷結束，沒有發現循環
        return False

##題目重點    
# 1.Optional 是 Python 中的一個型別提示，表示某個變數可以是
# 指定的型別（像這題是ListNode），或者是 None。
# 2.使用一個快指針，一個慢指針的理由：

#   情況1：當快指針和慢指針在不同速度上移動時，
#   如果存在循環，快指針總是會比慢指針多走一些路，最終它會「追上」慢指針，並在某個點相遇。

#   情況2：如果沒有循環，快指針將很快走到鏈結串列的末尾（即 None），
#   這時我們就知道鏈結串列是線性的，沒有循環
#   且快指針每次走兩步，慢指針每次走一步是最佳設置
