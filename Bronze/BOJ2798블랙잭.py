# #BOJ2798_블랙잭_B2
# #https://www.acmicpc.net/problem/2798

# # N개의 숫자가 담겨있는 arr중 3개만 뽑은 조합인데, sort할 때 겹치면 안됨
# # 순열로 뽑고, 그걸 합들을 arr에 모두 담는다

# # 혹은 그냥 3개씩 뽑고 더한 값을 arr에 담고
# # m을 넘으면 버리고, m 안에 있으면 담아서 마지막값을 뽑는다.

n, m= map(int, input().split())
arr = list(map(int, input().split()))
result = 0 

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])

print(result)

