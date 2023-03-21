#BOJ16238_Farm_B2
#https://www.acmicpc.net/problem/16283

a, b, n, w = map(int, input().split()) 
check = 0
numA, numB = 0,0

#범위에 주의 
for i in range(1, n):
    #1~n-1까지 돌면서 w와 일치하는 값이 발생하는지 조사
    #n-1로 해야 0이 발생하지 않는다.
    if a*i + b*(n-i) == w:
        check += 1
        numA = i
        numB = n-i

if check == 1: 
    print(numA, numB)

else:
    print('-1') 