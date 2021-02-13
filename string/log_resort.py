# 로그 재정렬
# 기준) 1. 가장 앞 부분은 식별자
#       2. 문자로 구성된 로그가 숫자 로그보다 앞에 옴
#       3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순
#       4. 숫자 로그는 입력 순서대로 함

# lambda, + 연산자 이용
def solution(logs):
    digit_log = []
    str_log = []

    for log in logs:
        if log.split()[1].isdigit():
            digit_log.append(log)
        else:
            str_log.append(log)
    
    str_log.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 알파벳 순 정렬, 동일한 경우 식별자로
    
    print(str_log + digit_log)


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

solution(logs)

