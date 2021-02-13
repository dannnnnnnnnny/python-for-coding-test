## 인접 행렬

# INF = 999999999

# graph = [
#     [0, 7, 5],
#     [7, 0 , INF],
#     [5, INF, 0]
# ]

# print(graph)

#-------------------------------------------------------

## 인접 리스트

# graph = [[] for _ in range(3)]

# graph[0].append((1, 7))
# graph[0].append((2, 5))

# graph[1].append((0, 7))

# graph[2].append((0, 5))

# print(graph)

#-------------------------------------------------------

# # DFS 함수 정의
# # * 깊이우선탐색
# # 한번 방문하면 깊게 쭉 방문하고 나옴
# # 스택 자료구조 이용, 재귀 함수 이용

# def dfs(graph, v, visited):
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
    

# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph = [
#   [],
#   [2, 3, 8],
#   [1, 7],
#   [1, 4, 5],
#   [3, 5],
#   [3, 4],
#   [7],
#   [2, 6, 8],
#   [1, 7]
# ]

# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 9

# # 정의된 DFS 함수 호출
# dfs(graph, 1, visited)


#-------------------------------------------------------


# # BFS 함수 정의
# # * 너비우선탐색
# # 가까운 노드부터 탐색
# # 큐 자료구조 이용 (파이썬 Deque 라이브러리)

# from collections import deque

# def bfs(graph, start, visited):
#     # Queue 구현을 위한 deque
#     queue = deque([start])

#     # 현재 노드 방문 처리
#     visited[start] = True

#     # 큐가 빌 때까지 반복

#     while queue:
#         # 큐에서 하나의 원소를 뽑아서 출력
#         v = queue.popleft()
#         print(v, end=' ')

#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9

# bfs(graph, 1, visited)


#-------------------------------------------------------

# 음료수 얼려먹기
# DFS 문제

dx = [-1 , 1, 0 , 0]
dy = [0, 0, 1, -1]

graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

def dfs(x, y):

    if x <= -1 or x >= 4 or y <= -1 or y >= 5:
        return False

    if graph[x][y] == 0:

        graph[x][y] = 1

        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        
        return True

    return False


result = 0

for i in range(4):
    for j in range(5):

        if dfs(i, j) == True:
            result += 1


print(result)