#BOJ10987_모음의 개수_B3
#https://www.acmicpc.net/problem/10987

check = ['a' , 'e', 'i', 'o', 'u']
cnt = 0
for i in input():
    if i in check:
        cnt += 1
print(cnt)