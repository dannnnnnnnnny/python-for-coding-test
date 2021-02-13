## Palindrome Liked list


def solution(data):
    q = []

    if not data:
        return True
    
    while data is not None and data:
        if data.pop(0) == data.pop():
            continue
        
        else:
            return False

    return True

print(solution([1,2,2,1])) 