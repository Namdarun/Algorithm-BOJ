#BOJ11399_ATM
N = int(input())
P = list(map(int, input().split()))
#작은 순으로 정렬
P.sort()
result = 0

#리스트의 N까지 더해줌
for i in range(1, N+1):
    result += sum(P[0:i])

print(result)