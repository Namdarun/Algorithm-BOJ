#BOJ22351_수학은 체육과목입니다 3
#https://www.acmicpc.net/problem/22351
# rstrip를 추가해야 정상적으로 답이 나오는 이유...
# readline?
# 처음수부터 시작해서 하나씩 더하고, 입력길이와 같아질때까지 더해준다
# 입력길이가 같아지면 처음과 끝수 도출 

import sys
input = sys.stdin.readline
s = input().rstrip()

for i in range(1, len(s)+1):
    # 잘라서 비교하기 위한 변수
    # 처음 수
    ss = s[:i]
    # 마지막 수 
    n = int(ss)

    while len(ss) < len(s):
        n +=1
        ss+= str(n)
    # 길이가 같아지면 처음수와 끝수-문자처리 후 도출
    if ss == s:
        print(ss[:i] + ' ' + str(n))
        exit()

