# 1 만들기
x = 26
dp = [0] * 100
def make_one(x):
  for i in range(2, x+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
      dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
      dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
      dp[i] = min(dp[i], dp[i // 5] + 1)
  return dp[x]

print(make_one(x))


# 개미 전사
ant_data = [1, 3, 1, 5]
dp = [0] * 100
def ant(data):
  dp[0] = data[0]
  dp[1] = max(data[0], data[1])

  for i in range(2, len(data)):
    dp[i] = max(dp[i-1], dp[i-2]+data[i])
  
  return dp[3]
print(ant(ant_data))


# 바닥 공사
def floor_work(x):
  dp = [0] * 100
  dp[1] = 1
  dp[2] = 3

  for i in range(3, x + 1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796
  
  print(dp[x])

floor_work(3)


def floor_work2(x):
  dp = [0] * 100
  dp[1] = 2
  dp[2] = 5

  for i in range(3, x + 1):
    dp[i] = (dp[i-1]*2 + dp[i-2] * 5) % 796796
  
  print(dp[x])

floor_work2(3)


print('########min_money')
n = 3
money = [2, 3, 5]
m = 7
def min_money(n, m):
  d = [10001] * (m+1)

  d[0] = 0  # 0원을 만들 수 있는 화폐 갯수 0

  for i in money: # 화폐 단위 (2, 3, 5)
    for j in range(i, m + 1): # 가장 낮은 화폐 단위부터 만들어야할 화폐 m 까지
      if d[j-i] != 10001: # 해당 값을 만들기 전 (eg. 2원을 만들기 위해선 2원을 뺀 0원을 만들 수 있어야함. 0원은 0개)
        d[j] = min(d[j], d[j-i] + 1)


  if d[m] == 10001:
    print(-1)

  return print(d[m])

min_money(n, m)


# 우선순위 큐 다익스트라
print("###### 다익스트라")
import heapq

# n: 노드 수, m: 간선 수
n = 6
m = 11
# data = [[1, 2, 2], [1, 3, 5], [1, 4, 1], [2, 3, 3], [2, 4, 2], [3, 2, 3], [3, 6, 5], [4, 3, 3], [4, 5, 1], [5, 3, 1], [5, 6, 2]]
graph = [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]
distance = [int(1e9)] * (n+1)

def dijkstra(start):
  q = []
  
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q: # 큐가 비어있지않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    
    # 이미 처리한 노드라면 무시
    if distance[now] < dist:
      continue

    # 현재 노드와 연결된 다른 인접한 노드 확인
    for i in graph[now]:
      cost = dist + i[1]  # i[1] : 거리
      
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0])) # i[0] : 노드 번호
    print(q)
dijkstra(1)

for i in range(1, n+1):
  # 도달할 수 없는 경우, 무한이라고 출력
  if distance[i] == int(1e9):
    print('무한')
  else:
    print(distance[i])
