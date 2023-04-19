#BOJ2407_조합_S3
#https://www.acmicpc.net/problem/2407

def factorial(a):
    cnt = 1
    for i in range(2, a+1):
        cnt *= i
    return cnt

n, m = map(int, input().split())

#분모를 감싸줘야함에 주의하자
print(factorial(n)//(factorial(m)*factorial(n-m)))
    