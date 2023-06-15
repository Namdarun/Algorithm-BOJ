#BOJ1977_완전제곱수_B
#https://www.acmicpc.net/problem/1977

m = int(input())
n = int(input())

hap = 0
check = 0

for i in range(1, 101):
    if m <= i*i and n >= i*i:
        if hap == 0:
            check = i*i
        hap += i*i

if hap == 0:
    print(-1)

else:
    print(hap)
    print(check)