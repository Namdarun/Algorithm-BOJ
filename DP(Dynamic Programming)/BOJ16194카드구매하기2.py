#BOJ16194_카드구매하기2
#https://www.acmicpc.net/problem/16194

# n개의 카드를 구매하기 위한 최소장수
n = int(input())
#인덱스로 인해 각각 0과 n+1로 놔준다
price = [0] + list(map(int, input().split()))
# 확인을 위한 불린값 
dp = [False for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        if dp[i] == False:
            dp[i] = dp[i-j]+price[j]
            # print(dp)
            # print(dp[i])
        else:
            dp[i] = min(dp[i], dp[i-j]+price[j])
            # print(dp)
            # print(dp[i])

print(dp[i])