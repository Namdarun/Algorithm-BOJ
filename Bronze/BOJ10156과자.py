#BOJ10156_과자_B4
#https://www.acmicpc.net/problem/10156

k, n, m = map(int, input().split())
result = (k*n)-m

print(result if result > 0 else 0)