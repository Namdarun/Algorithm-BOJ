#BOJ10799_쇠막대기_S2
#https://www.acmicpc.net/problem/10799

import sys
input = sys.stdin.readline

#rstrip 주의 
stick = list(input().rstrip())
#답
result = 0
#스택
li = []

for i in range(len(stick)):
    if stick[i] == '(':
        li.append('(')

    #닫는괄호일때 
    else:
        #레이저 = stack에 쌓인 쇠막대기 개수만큼 추가
        if stick[i-1] == '(':
            li.pop()
            result += len(li)
        
        #쇠막대기 끝 = 하나씩만 추가 
        else:
            li.pop()
            result += 1
print(result)



