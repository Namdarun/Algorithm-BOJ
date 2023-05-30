#BOJ1003_피보나치수_S3
#https://www.acmicpc.net/problem/1003

# 함수를 사용해보자
n = int(input())
for i in range(n):
    num = int(input())
    s, e = 1, 0
    for j in range(num):
        s, e = e, s+e
    
    print(s, e)