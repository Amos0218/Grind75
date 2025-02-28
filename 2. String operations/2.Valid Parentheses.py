# 	題目要求你判斷一個由括號組成的字串是否有效


class Solution:
    def isValid(self,s: str) -> bool:
        stack = [] # 用來存放開括號的堆疊

        # 遍歷字符串中的每個字符
        for char in s:
            if char in "({[":  # 如果是開括號
                stack.append(char)  # 把它推入堆疊
            else:
                # 檢查堆疊是否為空(False)，或者當前字符是否匹配堆疊頂部的開括號
                top_element = stack.pop() if stack else '#'
                if char == ')' and top_element != '(':  # 如果是閉括號 ')'
                    return False
                elif char == '}' and top_element != '{':  # 如果是閉括號 '}'
                    return False
                elif char == ']' and top_element != '[':  # 如果是閉括號 ']'
                    return False

        return not stack  # 如果堆疊為空，表示所有的括號都匹配了，回傳True
    
##題目重點
#1.  堆疊（Stack）資料結構：後進先出，所以推疊頂部就是之前最後加入的元素
#2.  在Python中，list如果為空，則會回傳False，反之，如果有東西，則會回傳True
#3.  .pop()會先刪除清單中最後的元素再返回被刪除元素的值，如果你沒有指定另一個變數，那就是單純的刪除
