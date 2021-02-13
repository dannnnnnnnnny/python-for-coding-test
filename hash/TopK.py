# 상위 K 빈도 요소

nums = [1, 1, 1, 2, 2, 3]
k = 2

from collections import Counter
def solution(nums, k):
    print(list(zip(*Counter(nums).most_common(k)))[0])

    #print([key for key, value in dic.items() if value >= k])


solution(nums, k)
