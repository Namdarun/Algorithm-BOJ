#BOJ1296_팀이름정하기_B1
#https://www.acmicpc.net/problem/1296

name = input()
n = int(input())
li = sorted([input() for _ in range(n)])
a = b = 0
for i in range(n):
    l = name.count('L') + li[i].count('L')
    o = name.count('O') + li[i].count('O')
    v = name.count('V') + li[i].count('V')
    e = name.count('E') + li[i].count('E')
    check = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100
    if a < check:
        a = check
        b = i

print(li[b])