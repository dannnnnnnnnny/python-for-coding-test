# 가장 흔한 단어
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력
# 대소문자 구분하지 않고, 구두점 무시

import re
import collections

def solution(paragraph, banned):

   # ^\w는 단어 문자가 아닌 모든 문자
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                if word not in banned]
    
    count = collections.Counter(words)
    print(max(count, key=count.get))
    print(count.most_common(1)[0][0])

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

solution(paragraph, banned)