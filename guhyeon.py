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

#----------------------------------------------------------------------------
# 럭키스트레이트
# 123402 => 반 나눠서 왼합, 오합이 같으면 LUCKY, 아니면 READY
print('럭키 스트레이트')

def lucky(data):
    answer = 'READY'
    n = int(len(data)/2)

    if sum(list(map(int, list(data[:n])))) == sum(list(map(int, list(data[n:])))):
        return 'LUCKY'

    return answer 

print(lucky('123402'))


# 문자열 재정렬
print('문자열 재정렬')
data = 'AJKDLSI412K4JSJ9D'
def solution(data):
    num = 0
    idx = 0
    data = list(data)
    data.sort()
    print(data)

    for i in range(len(data)):
        if data[i].isdigit():
            num += int(data[i])
        else:
            idx = i
            break
    data = data[idx:] + [str(num)]
    print(''.join(data)) 
solution(data)

# 문자열 압축
'''
2020 카카오공채에 출제되었던 문제이다. 
먼저 문자열을 몇개 단위로 짜를지에 대해 step을 이용하는 제일 바깥 for문을 1, len(s) // 2 + 1까지 반복했다. 
문자열을 꼭 2로 나누어 문자열 길이보다 더 넘어가는 비교는 할 필요 없도록 한다. 
그리고 tempStr에 step만큼 짤라낸 문자열을 대입해 다음 문자열들과 step 단위로 비교한다.
(s[i:i+step]) 같으면 count를 +1 해주고, 틀리면 count와 비교했던 tempStr을 result값에 넣어주면 된다. 
그리고 중요한 것이 마지막에 한번 더 result에 count + tempStr을 넣어줘야 제일 마지막으로 비교했던 문자열이 들어갈 수 있다.
'''
print("문자열 압축")
data = 'aabbaccc'

def solution2(s):
    answer = 1000000
    for step in range(1, len(s) // 2 + 1):
        res = ''
        cnt = 1
        tmp = s[:step]

        for i in range(step, len(s) + step, step):
            print('step : ', step, end=' ')
            print('i : ', i, end=' ')
            print('s[', i, ':', i, '+', step, '] = ', s[i:i+step], end=' ')
            print('tmp : ', tmp, end=' ') 
            print('cnt : ', cnt, end=' ')
            print('res : ', res)
            if tmp == s[i : i + step]:
                cnt += 1

            else:
                if cnt == 1:
                    res += tmp
                else:
                    res = res + str(cnt) + tmp
                
                tmp = s[i : i + step]
                cnt = 1

        answer = min(answer, len(res))
    
    return answer
print(solution2(data))    

print('치킨 배달')
from itertools import combinations

n = 5
m = 3
data = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2]
]

def solution3(n, m, data):
    chicken = []
    house = []

    for r in range(len(data)):
        for c in range(n):
            if data[r][c] == 1:
                house.append((r, c))
            elif data[r][c] == 2:
                chicken.append((r, c))
    
    print(house)
    print(chicken)
    candidates = list(combinations(chicken, m))
    print("candi : ", candidates)
    def get_sum(candidate):
        result = 0

        for hx, hy in house:
            temp = 1e9
            for cx, cy in candidate:
                temp = min(temp, abs(hx - cx) + abs(hy - cy))
            
            result += temp
        
        return result
    
    result = 1e9
    for candidate in candidates:
        result = min(result, get_sum(candidate))
    
    print(result)

solution3(n, m, data)