from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            elif char == "+":    
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif char == "-":    
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif char == "*":    
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)        
            else:  # "/"
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a) if b * a >= 0 else -(-b // a))  # ✅ 修正負數情況(以防他一直往負的方向取整)
        
        return stack.pop()  # ✅ 正確返回結果

##題目重點
# 1.堆疊是後進先出，所以進行運算時是b在前a在後
# 2.在修正負數那行的展開為
#    if b * a >= 0:  # 兩個數同號，正常整數除法
#       result = int(b / a)
#    else:  # 兩個數異號，手動修正
#       result = -(-b // a)    
# 3. 向零取整：捨去小數部分，直接保留整數
#    向下取整：永遠往負無窮方向取整