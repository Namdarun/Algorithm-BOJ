#BOJ10162_전자레인지_B3
#https://www.acmicpc.net/problem/10162

n = int(input())
if n % 10 != 0:
    print(-1)

else:
    for i in [300, 60, 10]:
        print(n//i, end=' ')
        n = n%i