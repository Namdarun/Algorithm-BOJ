#BOJ16970_정수좌표의개수_S1
#https://www.acmicpc.net/problem/16970

def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

#첫번째 예제 
#1, 1안에서 2개의 정수로 된 점을 찍는데,
#k개 지나는 선분들을 구함
cnt = 0 
n, m, k = map(int, input().split())
#최대공약수 측정
result = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(1, n+1):
            for l in range(1, m+1):
                if gcd(k-i, l-j) == k:
                    result += 1

print(result)