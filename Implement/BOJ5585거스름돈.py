#BOJ5585_거스름돈_B2
#https://www.acmicpc.net/problem/5585

#잔돈의 개수, 500원부터 넣고 카운트는 몫으로
a = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
count = 0
for i in b:
    count += a // i
    a %= i
print(count)