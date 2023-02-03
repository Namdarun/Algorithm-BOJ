#BOJ10870_피보나치수5
#https://www.acmicpc.net/problem/10870

#재귀
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))