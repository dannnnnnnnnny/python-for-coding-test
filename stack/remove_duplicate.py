# 중복 문자 제거

# 1) 재귀

def solution(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]

        if set(s) == set(suffix):
            return char + solution(suffix.replace(char, ''))
    
    return ''

s = 'cbacdcbc'
print(solution(s))

# 2) 스택 사용
from collections import Counter
def solution2(s):
    counter = Counter(s)
    stack = []

    for char in s:
        counter[char] -= 1
        
        if char in stack:
            continue

        # char가 이전 문자보다 앞선 문자이고, 뒤에 붙일 문자가 남아있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()
        stack.append(char)
    
    print(stack)

solution2(s)