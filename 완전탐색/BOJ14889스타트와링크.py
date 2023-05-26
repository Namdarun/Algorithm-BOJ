#BOJ14889_스타트와링크_S2
#https://www.acmicpc.net/problem/14889

#백트래킹 -> 재귀로 돌리자
#두 팀으로 나눠서 방문처리
#명수가 n//2로 채워지면 각 팀 능력치 구함
#능력치 차이의 절대값과 최소값을 비교하면서 갱신하기

def dfs(x, y):
    global result
    if x == n // 2:
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += arr[i][j]
                elif not visited[i] and not visited[j]:
                    b += arr[i][j]
        
        result = min(result, abs(a-b))
        return

    for i in range(y, n):
        if not visited[i]:
            visited[i] = True
            dfs(x+1, i+1)
            visited[i] = False

n = int(input())
visited = [False for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]
result = int(1e9)

dfs(0, 0)
print(result)
                
                