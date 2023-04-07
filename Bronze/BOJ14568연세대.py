#BOJ14568_연세대학교_B3
#https://www.acmicpc.net/problem/14568

#n개를 3명한테 나누는 법을 고민 

n = int(input())
cnt = 0
for i in range(1, n//2):
    for j in range(1, n):
        if 2*i+2*j+2<=n:
            cnt += 1

print(cnt)