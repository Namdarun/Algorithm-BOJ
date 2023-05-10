#BOJ15666_N과M12_S2
#https://www.acmicpc.net/problem/15666

#N개 중 M개 수열, 같은 수 중복 가능, 비내림차순

def dfs(num):
    if len(arr) == m:
        print(*arr)
        return
    cnt = 0
    for i in range(num, n):
        if cnt != nums[i]:
            arr.append(nums[i])
            cnt = nums[i]
            dfs(i)
            arr.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = []

dfs(0)