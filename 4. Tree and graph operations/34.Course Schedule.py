from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 1️⃣ graph[prereq] 存放所有要依賴prereq 的course（初始化為空列表）
        graph = [[] for _ in range(numCourses)]  
        indegree = [0] * numCourses  # indegree[i] 表示課程 i 的入度 (有多少課程依賴它)

        # 2️⃣ 填充鄰接表與入度陣列
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # 例如 [1, 0] 表示 0 → 1
            indegree[course] += 1  # 目標課程的入度增加

        # queue 負責存「目前可以修的課程」，也就是 入度為 0 的課程
        queue = [i for i in range(numCourses) if indegree[i] == 0]

        # 使用 BFS 進行拓撲排序
        count = 0  # 記錄已經修過的課程數
        while queue:
            curr = queue.pop(0)  # 取出當前可以修的課程
            count += 1  # 修完這門課，計數 +1

            # 3️⃣ 遍歷所有依賴當前課程（curr)的課程 (curr → neighbor)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1  # 這門課修完了，所以依賴curr的課程（neighbor)的入度應該減少 -1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)  # 如果入度變為 0，則加入 queue (代表可以修了)

        # 4️⃣ 如果修過的課程數等於總課程數，則可以修完所有課程
        return count == numCourses
    
##題目重點     
#  1. prerequisites: List[List[int]], 先修課程對應關係 [a, b]，表示「要修 a 必須先修 b 」
#  在 4️⃣ 中，如果回傳為
#   • True → 所有課程都能修完，即 圖中無環 。
# 	• False → 無法修完所有課程，即 圖中存在環 (有課程的前置條件相互依賴，導致死循環)
       