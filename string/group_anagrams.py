# 그룹 애너그램
# 문자열 배열을 받아 애너그램 단위로 그룹핑

# 애너그램 : 언어유희로, 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
data = ["eat", "tea", "tan", "ate", "nat", "bat"]

# 1) 정렬하여 딕셔너리에 추가
# 정렬하면 같은 값을 갖게되기 때문
import collections

def solution(data):
    anagrams = collections.defaultdict(list)

    for word in data:
        anagrams[''.join(sorted(word))].append(word)
    
    return anagrams.values()

print(solution(data))