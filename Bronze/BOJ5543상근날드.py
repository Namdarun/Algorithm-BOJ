#BOJ5543_상근날드_B4
#https://www.acmicpc.net/problem/5543

a = 2000
c = 2000
for i in range(3):
    b = int(input())
    a = min(a, b)
for i in range(2):
    b = int(input())
    c = min(c, b)
print(a + c - 50)