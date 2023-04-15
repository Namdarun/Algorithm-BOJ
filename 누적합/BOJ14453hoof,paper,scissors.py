#BOJ14453_Hoof, paper, scissors
#https://www.acmicpc.net/problem/14453

#가위바위보 아류작 / 발굽, 종이, 가위 
# 발굽 > 가위 > 종이 > 발굽
# 처음이 발굽, 전체게임에서 한번만 제스처 전환 
# 발굽을 플레이한 다음 나머지 게임에 대해 다른 걸로 전환가능
# 최대 이길 수 있는 수

n = int(input())
# 인덱스를 위해 0 추가하고, 각 알파벳에 따라 해당 배열에 넣어줌 
h = [0] * (n + 1)
p = [0] * (n + 1)
s = [0] * (n + 1)
for i in range(n):
    a = input()
    if a == "H":
        h[i+1] = h[i] + 1
        p[i+1] = p[i]
        s[i+1] = s[i]
    elif a == "P":
        h[i+1] = h[i]
        p[i+1] = p[i] + 1
        s[i+1] = s[i]
    elif a == "S":
        h[i+1] = h[i]
        p[i+1] = p[i]
        s[i+1] = s[i] + 1


prefix = [0] * (n + 1)

for i in range(1, n+1):
    prefix[i] = h[i] + p[i] + s[i]

answer = 0

for i in range(n+1):
    hh = h[i] + (s[n] - s[i])
    pp = p[i] + (h[n] - h[i])
    ss = s[i] + (p[n] - p[i])
    answer = max(answer, hh+pp+ss)

print(answer)