#BOJ17413_단어뒤집기2.py
#https://www.acmicpc.net/problem/17413

import sys
input = sys.stdin.readline
#오른쪽 공백 지우기 
s = input().rstrip()
ans = ""
#<>인지 체크
tag = False
stack = ""
for i in s:
    #<>안에 있는 문자열 그대로 출력 
    if i == "<":
        tag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        tag = False
        ans += i
        continue
    #공백이 있을 경우 뒤집어서 출력 
    elif i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue
        
    #그 밖 문자열은 스택에 담고 
    if tag:
        ans += i
    else:
        stack += i

print(ans+stack[::-1])
