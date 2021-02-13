# 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스 리턴

nums = [2, 7, 11, 15]
target = 9

# 1) 브루트 포스 방식 (무차별 대입), O(n^2)
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(solution(nums, target))


# 2) in을 이용한 탐색
# 모든 조합을 비교하지 않고, target에서 첫번째 값을 뺀 값 target - n 값이
# 존재하는지 검색
# O(n^2) 이지만 in 연산이 훨씬 더 가볍고 빠름.

def solution2(nums, target):
    for i, n in enumerate(nums):
        comp = target - n

        if comp in nums[i+1:]:
            return [i, nums.index(comp)]

print(solution2(nums, target))


# 3) 첫 번째 수를 뺀 결과 키 조회
# 해시 테이블 이용
# 평균적으로 O(1), 최악의 경우 O(N)


def solution3(nums, target):
    dic = {}

    for i, num in enumerate(nums):
        dic[num] = i    # 인덱스를 값으로 가짐
    
    for i, num in enumerate(nums):
        if target-num in dic and dic[target-num] != i:
            return [dic[num], dic[target-num]]


print(solution3(nums, target))


# 4) 3에서 조회 구조 개선
def solution4(nums, target):
    dic = {}

    for i, num in enumerate(nums):
        if target-num in dic:
            return [dic[target-num], i]
        dic[num] = i
print(solution4(nums, target))


# 5) 투 포인터 이용
# 양쪽에 포인터를 두고, 그 합이 target보다 작으면 왼쪽 포인터를 우측 이동
# target보다 크면 오른쪽 포인터를 왼쪽 이동시키며 찾음
# But, nums가 정렬이 안되어있다면 소용 없음
#  
def solution5(nums, target):
    left, right = 0, len(nums)-1

    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right] 


print(solution5(nums, target))