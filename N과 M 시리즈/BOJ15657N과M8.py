#BOJ15657_N과M8_S3
#https://www.acmicpc.net/problem/15657

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    # 중복불가
    for i in range(start, n):
            s.append(nums[i])
            dfs(i)
            s.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
dfs(0)