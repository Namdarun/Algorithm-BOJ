#BOJ11557_Yangjojang_B1
#https://www.acmicpc.net/problem/11557

#단순구현
t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    check_name = ''
    for _ in range(n):
        name, b = input().split()
        b = int(b)
        if b > result:
            result = b
            check_name = name
    
    print(check_name)