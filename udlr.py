# up / down / left / right
# n = 5
# datas = ['R', 'R', 'R', 'U', 'D', 'D']
# def solution(n, datas):
#   answer = [1, 1]
#   dic = {
#     'U' : [-1, 0],
#     'D' : [1, 0],
#     'L' : [0, -1],
#     'R' : [0, 1]
#   }

#   for data in datas:
#     if answer[0] + dic[data][0] > 0 and answer[0] + dic[data][0] <= n:
#       if answer[1] + dic[data][1] > 0 and answer[1] + dic[data][1] <= n:
#         answer[0] += dic[data][0]
#         answer[1] += dic[data][1]


#   return answer

# print(solution(n, datas))


