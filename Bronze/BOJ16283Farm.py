#BOJ16283_Farm_B2
#https://www.acmicpc.net/problem/16283

a, b, n, w = map(int, input().split()) 
check = 0
result_a, result_b = 0,0

for i in range(1, n):
    if a*i + b*(n-i) == w:
        check += 1
        result_a = i
        result_b = n-i

print(result_a, result_b if check == 1 else '-1')