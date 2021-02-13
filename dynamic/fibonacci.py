# n이 커지면 커질수록 수행시간이 기하급수적으로 올라감
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

# 메모이제이션 기법
# (탑다운)
# 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법 (캐싱이라고도 함)
d = [0] * 20

def fibo_topdown(n):
  if n == 1 or n == 2:
    return 1
  
  if d[n] != 0:
    return d[n]
  
  d[n] = fibo_topdown(n-1) + fibo_topdown(n-2)
  print(d)
  return d[n]

print(fibo_topdown(10))

# (바텀업)
data = [0] * 20
data[0] = 0
data[1] = 1

def fibo_bottomup(n):
  i = 2
  while i <= n:
    data[i] = data[i-1] + data[i-2]
    i += 1

  return data[n]

print(fibo_bottomup(10))