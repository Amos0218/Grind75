# 用 兩個堆疊（Stacks） 來 實作佇列（Queue）

class MyQueue:

    def __init__(self):
        self.stack1 = []  # 用於存放新進的元素
        self.stack2 = []  # 用於提供正確的 FIFO 出列順序

    def push(self, x: int) -> None:
        """將元素 x 加入佇列的尾端"""
        self.stack1.append(x)

    def pop(self) -> int:
        """移除佇列前端的元素並返回"""
        if not self.stack2:     # 當 stack2 為空時，將 stack1 的元素倒入 stack2
            while self.stack1:
                #從 stack1 取出最上層的元素，放進 stack2
                self.stack2.append(self.stack1.pop()) 
        return self.stack2.pop()  

    def peek(self) -> int:
        """回傳佇列前端的元素，但不移除"""
        if not self.stack2:  # 如果 stack2 為空，先轉移元素
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]  # 返回 stack2 最後面的元素

    def empty(self) -> bool:
        """如果佇列為空，返回 True，否則返回 False"""
        return not self.stack1 and not self.stack2  # 兩個 stack 都為空才回傳 True
    
    ##題目重點
    # 1.兩個堆疊組合：
	#   stack1 負責「新進元素」，但它是 LIFO後進先出(堆疊)。
	#   當 stack1 的元素全部轉移到 stack2，順序會反轉，就變成 FIFO先進先出(佇列)。
	#   所以最後 stack2.pop() 取得 stack2 的最上方元素時，
    #   就會是原本 stack1 最早進來的元素，模擬了佇列的行為。