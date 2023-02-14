#BOJ2475_검증된 수 
#https://www.acmicpc.net/problem/2475
res = 0
for n in list(map(int, input().split())):
    res += n**2
print(res%10)