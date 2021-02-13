# 주어진 문자열이 팰린드롬인지 확인 ( 대소문자 구분X, 영문자와 숫자만 대상 )

# # 1) 리스트
# def solution(str):
#     data = []
#     for s in str:
#         if s.isalnum():
#             data.append(s.lower())

#     while len(data) > 1:
#         if data.pop(0) != data.pop():
#             return False
    
#     return True


# # 2) Deque
# # pop(0)은 O(N)인데 반해, deque의 popleft()는 O(1)이라 훨씬 빠름
# from collections import deque

# def solution(str):
#     data = deque()

#     for s in str:
#         if s.isalnum():
#             data.append(s.lower())
    
#     while len(data) > 1:
#         if data.popleft() != data.pop():
#             return False

#     return True



# 3) 슬라이싱
# [::-1] 로 리스트를 뒤집을 수 있으며, 내부적으로 C로 구현되어 있어서
# deque 보다도 더 빠른 속도를 기대할 수 있음.

def solution(str):
    data = []
    
    for s in str:
        if s.isalnum():
            data.append(s.lower())
    # 또는
    # import re
    # str = str.lower()
    # str = re.sub('[^a-z0-9]', '', str)    # 소문자나 숫자가 아니면 공백으로 변경
    # return str == str[::-1]

    return data == data[::-1]




print(solution("A man, a plan, a canal: Panama"))