arr = [14, 7, 3, 12, 9, 11, 6, 2]


# 버블 정렬
# for i in range(len(arr)):
#     for j in range(1, len(arr)-i):
#         if arr[j-1] > arr[j]:
#             temp = arr[j-1]
#             arr[j-1] = arr[j]
#             arr[j] = temp
#     print(arr)
# print(arr)


# 선택 정렬
# for i in range(len(arr)-1):
#     idx = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[idx]:
#             idx = j

#     temp = arr[idx]
#     arr[idx] = arr[i]
#     arr[i] = temp
# print(arr)



# # 퀵 정렬
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr)+equal_arr+quick_sort(greater_arr)

# print(quick_sort(arr))


# # 병합 정렬
# def merge_sort(arr):
    
#     if len(arr) < 2:
#         return arr
    
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     result = []
#     l, r = 0, 0
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     result += left[l:]
#     result += right[r:]
    
#     return result

# print(merge_sort(arr))


# # 힙 정렬
# def heapify(arr, index, size):
#     largest = index
#     left_index = 2 * index + 1
#     right_index = 2 * index + 2

#     if left_index < size and arr[left_index] > arr[largest]:
#         largest = left_index
#     if right_index < size and arr[right_index] > arr[largest]:
#         largest = right_index

#     if largest != index: # 변경이 일어났다면
#         arr[largest], arr[index] = arr[index], arr[largest]
#         heapify(arr, largest, size)

# def heap_sort(arr):
#     for i in range(len(arr)//2-1, -1, -1):
#         heapify(arr, i, len(arr))
    
#     for i in range(len(arr)-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, 0, i)

#     return arr

# print(heap_sort(arr))


# 이분 탐색
arr2 = [1,3,4,6,7,9,11,12,15]
# def Binary_search(arr, n):

#     start = 0
#     end = len(arr) - 1

#     while start <= end:
#         mid = (start + end) // 2

#         if arr[mid] == n:
#             return mid 
        
#         elif arr[mid] > n:
#             end = mid - 1
        
#         elif arr[mid] < n:
#             start = mid + 1
        
# print(Binary_search(arr2, 3))

# 이분 탐색 재귀적 구현
def Binary_search2(arr, n, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == n:
        return mid

    elif arr[mid] > n:
        end = mid - 1
    else:
        start = mid + 1

    return Binary_search2(arr, n, start, end)

data = Binary_search2(arr2, 9, 0, 8)

print("data index : ", data)