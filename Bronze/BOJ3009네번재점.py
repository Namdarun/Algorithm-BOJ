#BOJ3009_네번째점
#https://www.acmicpc.net/problem/3009
#하나만 있는거 출력
a = []
b = []
for i in range(3):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
for i in range(3):
        if a.count(a[i]) == 1:
                x = a[i]
        if b.count(b[i]) == 1:
                y = b[i]
print(x, y)