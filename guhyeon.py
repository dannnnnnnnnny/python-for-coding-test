# # 구현
# # 1. 상하좌우 ((1,1)좌표에서 시작, data만큼 움직임. N은 N*N 맵 크기, 맵밖으로 나갈 수 없음)

# N = 5
# data = ['R', 'R', 'R', 'R', 'R', 'U', 'U', 'D', 'D', 'D']

# def solution(N, data):
#     dic = { 
#         'U': [-1, 0], 
#         'D': [1, 0,],
#         'L': [0, -1], 
#         'R': [0, 1] 
#     }

#     pos = [1, 1]

#     for d in data:
#         if pos[0] + dic[d][0] < 1 or pos[0] + dic[d][0] > N or pos[1] + dic[d][1] < 1 or pos[1] + dic[d][1] > N:
#             continue
#         pos[0] += dic[d][0]
#         pos[1] += dic[d][1]
    
#     print(pos)

# solution(N, data)

#-----------------------------------------------------------------------------------------------------

# # 2. 시각 ( 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되어 있으면 카운트 )

# N = 5

# def solution(N):
#     answer = 0
#     hour = range(N+1) # N에 따라 시간은 변화됨
#     minutes, seconds = range(60), range(60) # minute과 second는 항상 같음

#     for h in hour:
#         for m in minutes:
#             for s in seconds:
#                 if '3' in str(h)+str(m)+str(s):
#                     answer += 1
    
#     print(answer)

# solution(N)



#-----------------------------------------------------------------------------------------------------

# # 왕실의 나이트
# # 8x8 체스판, 나이트는 L자 형태로만 이동 가능, 정원 밖으로 나갈 수 없음
# # 수평으로 두 칸 이동후 수직으로 한칸 이동 or 수직으로 두 칸 이동 후 수직으로 한 칸 이동

# n = 8
# input = 'c2'

# def solution(n, input):
#     answer = 8
#     input = list(input)
    
#     col = int(ord(input[0])) - int(ord('a')) + 1
#     row = int(input[1])

#     moves = [[-2,1], [-2,1], [2,-1], [2,1], [-1,-2], [-1,2], [1,-2], [1,2]]

#     for move in moves:
#         n_col = col + move[0]
#         n_row = row + move[1]

#         if n_col > 8 or n_col < 1 or n_row > 8 or n_row < 1:
#             answer -= 1

#     print(answer)

# solution(n, input)


#-----------------------------------------------------------------------------------------------------

# 게임 개발
# N*M 직사각형 장소에서 각각 칸은 육지 또는 바다
# 캐릭터는 동서남북 중 한 곳을 바라봄
# 각 맵 칸은 (A, B)로 나타낼 수 있고, A는 북쪽에서부터 떨어진 칸 갯수, B는 서쪽으로부터 떨어진 칸 갯수
# 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간은 갈 수 없음.
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈곳 정함
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진.
# 3. 왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
# 4. 만약 네 방향이 모두 이미 가본 칸이거나 바다로 되어 있는 경우에는 바라보는 방향을 유지한채 한칸 뒤로가고 1단계로 돌아감
#     단, 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춤

# N = 4
# M = 4

# x, y, direction = 1, 1, 0

# d = [[0] * M for _ in range(N)]
# d[x][y] = 1 # 현재 위치 방문 처리

# array = [
#     [1, 1, 1, 1],
#     [1, 0 ,0, 1],
#     [1, 1, 0, 1],
#     [1, 1, 1, 1]
# ]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

# # 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#     # 왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else:
#         turn_time += 1
#     # 네 방향 모두 갈 수 없는 경우
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀있는 경우
#         else:
#             break
#         turn_time = 0

# # 정답 출력
# print(count)



#----------------------------------------------------------------------------------------------------
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