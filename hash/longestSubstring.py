# 중복 문자가 없는 가장 긴 부분의 문자열 길이 출력
# 슬라이딩 윈도우 & 투 포인터 사이즈 조절

string = "abcabcbb"

def solution(string):
    used = {}
    max_length = 0
    start = 0

    for idx, char in enumerate(string):
        # 이미 등장했던 문자 and 슬라이딩 윈도우 안쪽에 있는 중복 문자에 대해서
        #  start 위치를 현재 위치 + 1로 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:    # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, idx - start + 1)
        
        # 현재 문자의 위치 삽입
        used[char] = idx

    return max_length

print(solution(string))
