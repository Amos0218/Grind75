from collections import defaultdict

class TrieNode:
    def __init__(self):
        # 1️⃣
        self.children = defaultdict(TrieNode)  # 用 dict 取代陣列
        self.isEnd = False  # 是否為單詞結尾

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:         # 如果 char 存在於 children，就繼續往下走
            node = node.children[char]  
        node.isEnd = True     # 表示這個字母是word的最後一個字母

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:  # ❌ 找不到這個字母
                return False
            node = node.children[char]
        return node.isEnd  # ✅ 確保是完整的單詞

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # ✅ 這個前綴存在
    
##題目重點

#  ⭐️ Trie 的結構與概念
# 	•	Trie 是一種樹狀數據結構，用來快速查找單詞和前綴。
# 	•	透過 Trie，可以高效執行「單詞查找」與「前綴查找」。

#  ⭐️ TrieNode 是 Trie 樹中的基本單位，它存儲字母並指向其他字母，
#   TrieNode 代表的是 Trie 樹中的一個節點，
#   它包含了所有子節點的指向（children）以及是否為單詞結尾的標誌（isEnd）

#   在1️⃣中， defaultdict(TrieNode) 的意思是，當查詢一個不存在的鍵時，
#   defaultdict 會自動創建並返回一個新的 TrieNode 節點



