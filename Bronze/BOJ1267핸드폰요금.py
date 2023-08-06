#BOJ1267_핸드폰요금_B3
#https://www.acmicpc.net/problem/1267

n = int(input())
arr = list(map(int, input().split()))
y = m = 0
for i in arr:
    y += (i//30 + 1) * 10
    m += (i//60 + 1) * 15
if m == y:
    print("Y M", m)
elif m < y:
    print("M", m)
else:
    print("Y", y)