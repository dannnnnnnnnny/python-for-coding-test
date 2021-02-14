# 우선순위 큐 다익스트라
print("###### 다익스트라")
import heapq

# n: 노드 수, m: 간선 수
# n = 6
# m = 11
# data = [[1, 2, 2], [1, 3, 5], [1, 4, 1], [2, 3, 3], [2, 4, 2], [3, 2, 3], [3, 6, 5], [4, 3, 3], [4, 5, 1], [5, 3, 1], [5, 6, 2]]
# graph = [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]
# distance = [int(1e9)] * (n+1)

# def dijkstra(start):
#   q = []
  
#   # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
#   heapq.heappush(q, (0, start))
#   distance[start] = 0

#   while q: # 큐가 비어있지않다면
#     # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
#     dist, now = heapq.heappop(q)
    
#     # 이미 처리한 노드라면 무시
#     if distance[now] < dist:
#       continue

#     # 현재 노드와 연결된 다른 인접한 노드 확인
#     for i in graph[now]:
#       cost = dist + i[1]  # i[1] : 거리
      
#       # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
#       if cost < distance[i[0]]:
#         distance[i[0]] = cost
#         heapq.heappush(q, (cost, i[0])) # i[0] : 노드 번호
#     print(q)
# dijkstra(1)

# for i in range(1, n+1):
#   # 도달할 수 없는 경우, 무한이라고 출력
#   if distance[i] == int(1e9):
#     print('무한')
#   else:
#     print(distance[i])


# 플로이드 워셜 알고리즘
INF = int(1e9)

# n = 5
# m = 7
# graph = [[INF] * (n+1) for _ in range(n+1)]

# # 자기 자신에서 자기 자신으로 가는 비용은 0
# for a in range(1, n+1):
#   for b in range(1, n+1):
#     if a == b:
#       graph[a][b] = 0

# data = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [4, 5]]

# for d in data:
#   graph[d[0]][d[1]] = 1
#   graph[d[1]][d[0]] = 1

# # 거쳐갈 노드
# k = 5
# # 최종 목적지
# x = 4


# for z in range(1, n+1):
#   for a in range(1, n+1):
#     for b in range(1, n+1):
#       graph[a][b] = min(graph[a][b], graph[a][z] + graph[z][b])
# print(graph[1])
# print(graph[1][k])
# print(graph[k][x])
# distance = graph[1][k] + graph[k][x]

# if distance >= INF:
#   print("-1")
# else:
#   print(distance)


# 전보 p262
import heapq
INF = int(1e9)
n = 3
m = 2
start = 1
data = [[1, 2, 4], [1, 3, 2]]

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for d in data:
  graph[d[0]].append((d[1], d[2]))

def dijkstra(start):
  q = []

  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(len([i for i in distance if i != INF and i != 0]), max([i for i in distance if i != INF]))
