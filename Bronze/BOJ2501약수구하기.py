#BOJ2501_약수구하기_B3
#https://www.acmicpc.net/problem/2501

n, k = map(int, input().split())
arr = []
for i in range(1, n+1) :
    if n % i == 0 :
        arr.append(i)

if len(arr) < k :	# 약수의 개수가 K보다 작을 때
    print(0)
else :
    print(arr[k-1])	# 인덱스 번호에 맞춰서 k-1번째로 해야함