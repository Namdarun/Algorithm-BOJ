#BOJ1912_연속합_S2
#https://www.acmicpc.net/problem/1912

#누적합을 이용해보자

n = int(input())
arr = list(map(int, input().split()))

# 누적합 공식
prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

#최소로 표기
max_sum = -1000 
#최소 누적합
min_prefix_sum = 0  

# 각 구간의 합 중에서 최댓값 찾기
for i in range(1, n+1):
    max_sum = max(max_sum, prefix_sum[i] - min_prefix_sum)
    min_prefix_sum = min(min_prefix_sum, prefix_sum[i])

print(max_sum)