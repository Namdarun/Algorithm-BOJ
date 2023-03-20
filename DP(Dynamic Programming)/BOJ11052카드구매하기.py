#BOJ11052_카드구매하기1
#https://www.acmicpc.net/problem/11052

# n개의 카드를 구매하기 위한 금액의 최댓값 
n = int(input())
price = [0] + list(map(int, input().split()))
#인덱스로 인해 각각 0과 n+1로 놔준다
dp = [0 for _ in range(n+1)]

#인덱스로 인해 1부터 시작 
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+price[j])
print(dp[i])
