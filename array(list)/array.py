# 빗물 트래핑
# 투포인터 활용

def trap(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max = height[left]
    right_max = height[right]

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else: 
            volume += right_max - height[right]
            right -= 1

    return volume

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(height))

## 세 수의 합
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 요소 출력
def solution(nums):
    nums.sort()
    res = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left = i + 1
        right = len(nums) - 1

        while left < right:
            element_sum = nums[i] + nums[left] + nums[right]

            if element_sum < 0:
                left += 1
            elif element_sum > 0:
                right -= 1
            else:
                res.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1

    return res

nums = [-1, 0, 1, 2, -1, -4]

print(solution(nums))

