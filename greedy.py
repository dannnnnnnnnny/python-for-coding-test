# # 큰 수의 법칙
# # 테스트 케이스 
# # 1)
# data = [2,4,5,4,6]
# m = 8
# k = 3


# def solution(data, m, k):
#     answer = []
#     n = len(data)
#     data.sort()
#     i = 0

#     while i < m:
#         i += 1
#         if i % (k+1) == 0:
#             answer.append(data[n-2])
#         else:
#             answer.append(data[n-1])      
        
#     print(answer)
#     return sum(answer)

# print(solution(data, m, k))

#------------------------------------------------------------------------------------------------#

# # 숫자 카드 게임
# data = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]

# def solution(data):
#     m = 0
#     for d in data:
#         if m < min(d):    
#             m = min(d)
    
#     print(m)

# solution(data)

#----------------------------------------------------------------------------------------------#

# 1이 될 때 까지
# N = 25
# k = 5

# def solution(N, k):
#     cnt = 0
#     while N != 1:
#         if N % k == 0:
#             N //= k
#         else:
#             N -= 1
#         cnt += 1

#     print(cnt)

# solution(N, k)

# print(["foo", "bar", "baz"].index("a"))
isFind = 1

print(not isFind == 0)


#--------------------------------------------------------------------------------
# 모험가 길드
# N명의 모험가, 공포도가 각각 존재
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 함
print("모험가 길드")
n = 5
data = [2, 3, 1, 2, 2]

def solution(n, data):
    arr = [[] for _ in range(len(data)+1)]
    answer = 0
    data.sort()
    
    for i in range(len(data), 0, -1):
        arr[data[i-1]].append(data[i-1])

    arr = [i for i in arr if len(i) != 0]

    for i in arr:
        if i[0] <= len(i):
            answer += 1
    return answer

print(solution(n, data))


def g(n, data):
    res = 0
    cnt = 0

    for i in data:
        cnt += 1
        if cnt >= i:
            res += 1
            cnt = 0

    print(res)

g(n, data)

print('곱하기 혹은 더하기')
num = "02984"
def multi_add(num):
    answer = int(num[0])

    for i in range(1, len(num)):
        n = int(num[i])
        if n <= 1 or answer <= 1:
            answer += n
        else:
            answer *= n
    print(answer)
    return 0;

multi_add(num)

print('문자열 뒤집기')
str = "00011000"
def string_reverse(str):
    cnt0 = 0
    cnt1 = 0

    if str[0] == '1':
        cnt0 += 1
    else:
        cnt1 += 1
    
    for i in range(len(str) - 1):
        if str[i] != str[i+1]:
            if str[i+1] == '1':
                cnt0 += 1
            else:
                cnt1 += 1
        
    print(cnt0, cnt1)
string_reverse(str)


print('만들 수 없는 금액')
data = [3, 2, 1, 1, 9]
data.sort()
n = 5

target = 1

for x in data:
    if target < x:
        break
    target += x
    print("d : ", target)

print(target)


print('볼링공 고르기')
n = 8
m = 5
data = [1, 5, 4, 3, 2, 4, 5, 2]
answer = []

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] != data[j]:
            answer.append((i+1, j+1))

print(len(answer))


print('무지 먹방 라이브')
import heapq

n = 3
k = 15
data = [8, 6, 4]

q = []
for i in range(len(data)):
    heapq.heappush(q, (data[i], i+1))

print(q)

while q:
    dist, now = heapq.heappop(q)
    k -= dist * len(data)