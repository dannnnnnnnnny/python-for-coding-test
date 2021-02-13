# 일일 온도
# 매일의 화씨 온도를 체크해서 더 따뜻한 날씨를 위해서 며칠을 기다려야 하는지

T = [73, 74, 75, 71, 69, 72, 76, 73]

def solution(T):
    stack = []
    answer = [0] * len(T)

    for i, cursor in enumerate(T):
        while stack and cursor > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
        print(stack)
    print(answer)

solution(T)
    
    6348 3499 2072