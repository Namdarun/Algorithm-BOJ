# #BOJ16970_정수좌표의개수_S1
# #https://www.acmicpc.net/problem/16970
# #첫번째 예제 
# #1, 1안에서 2개의 정수로 된 점을 찍는데,
# #k개 지나는 선분들을 구함
n, m, k = map(int, input().split())
cnt = 0

def gcd(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b


# 가능한 모든 두 점에 대해 반복문 수행(완전탐색)
for i in range(n+1):
    for j in range(m+1):
        for a in range(i, n+1):
            for b in range(j, m+1):
                # 점 개수
                dx, dy = abs(a-i), abs(b-j)
                num = gcd(dx, dy)
                # 지나가는 점의 개수가 K개인 경우 count 증가
                if num == k:
                    cnt += 1

print(cnt)