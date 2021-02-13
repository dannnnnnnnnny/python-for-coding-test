# def binary_search(data, target, start, end):
#   while start <= end:
#     mid = (start + end) // 2

#     if data[mid] == target:
#       return True
#     elif data[mid] < target:
#       start = mid + 1
#     else:
#       end = mid - 1
#   return False

# data = [8, 3, 7, 9, 2]
# targets = [5, 7, 9]

# data.sort()

# for target in targets:
#   if binary_search(data, target, 0, len(data)-1):
#     print('yes')



# 떡이 [19, 10, 15, 17] cm씩 있을 때 손님에게 6cm를 주려면 몇cm의 절단기로 잘라야 하나? 
def binary_search(data, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    arr_sum = sum([x-mid if x-mid > 0 else 0 for x in data])
    print(mid, arr_sum)
    if target == arr_sum:
      return mid

    elif target < arr_sum:
      start = mid + 1
      
    else:
      end = mid - 1
  
  return 0
    

n = 6
data = [19, 15, 10, 17]
data.sort()


print(binary_search(data, n, 0, data[3]))