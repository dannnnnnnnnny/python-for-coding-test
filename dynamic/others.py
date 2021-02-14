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
