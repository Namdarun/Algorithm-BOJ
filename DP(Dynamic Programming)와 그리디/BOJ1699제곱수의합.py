#BOJ1699_제곱수의합_S2
#https://www.acmicpc.net/problem/1699

#top-down 방식으로 풀어보자 
# 근데 푼게 바텀업같은데...ㅠㅠ

n = int(input())
# i for i로 해야 답이 도출된다 -> 왜 그러지? 
dp = [i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        check = j*j
        # 제곱근을 넘어가면 멈추기
        if check > i:
            break

        # 항의 수를 최소로 찾아내가기
        if dp[i] > dp[i-check]+1:
            dp[i] = dp[i-check]+1

print(dp[n])