# J는 보석, S는 돌 / S에 보석이 몇개나 있을지
J = 'aA'
S = 'aAAbbbb'

from collections import Counter
def solution(J, S):
    count = 0

    res = Counter(S)
    
    for j in J:
        count += res[j]

    print(count)

solution(J, S) 

def solution2(J, S):
    return sum(s in J for s in S)

print(solution2(J, S))