def binary_search(data, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if data[mid] == target:
      return True
    elif data[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return False

data = [8, 3, 7, 9, 2]
targets = [5, 7, 9]

data.sort()

for target in targets:
  if binary_search(data, target, 0, len(data)-1):
    print('yes')