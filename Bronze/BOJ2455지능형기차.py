#BOJ2455_지능형기차_B3
#https://www.acmicpc.net/problem/2455

#단순구현

arr = []
person = 0

for i in range(4):
    a, b = map(int, input().split())
    person += b
    person -= a
    arr.append(person)

print(max(arr))


