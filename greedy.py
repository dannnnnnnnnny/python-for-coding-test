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