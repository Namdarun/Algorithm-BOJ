#BOJ1676_팩토리얼0의개수_S5
#https://www.acmicpc.net/problem/1676

#N!에서 뒤에서부터 0이고 처음 0이 나오지 않을때까지 0의 개수
#0이 되는 경우 2,5,10을 곱했을 때...
#그냥 팩토리얼로 일단 구해보자

from math import factorial
n = int(input())
cnt = 0 

for i in str(factorial(n))[::-1]:
    if i!= '0':
        break
    cnt += 1

print(cnt)