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
  print("dp : ", dp)
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