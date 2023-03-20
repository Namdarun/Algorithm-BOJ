#BOJ15645_내려가기2
#N이 10만 이하이므로 dp로 접근
import sys
input = sys.stdin.readline

N = int(input())
max_n = 0
min_n = 0
for i in range(N):
    num = list(map(int, input().split()))
    for j in range(3):
        while i <= N:
            if j == num[i][0]:
                max_n += max(num[i+1][0], num[i+1][1])
                max_n += min(num[i+1][0], num[i+1][1])
                i += 1

            elif j == num[i][1]:
                max_n += max(num[i+1][0], num[i+1][1], num[i+1][2])
                min_n += min(num[i+1][0], num[i+1][1], num[i+1][2])
                i += 1

            else: 
                max_n += max(num[i+1][1], num[i+1][2])
                min_n += min(num[i+1][1], num[i+1][2])
                i += 1

print(max_n)
print(min_n)