#BOJ11660_구간합구하기5_S1
#https://www.acmicpc.net/problem/11660

#1. 단순구현하면 되는 줄 알았는데, 시간초과가 났다. -> O(n**2)
#2. 시간복잡도를 줄이는 방법 : 구간합 (dp에 저장해서 필요한 부분만 더해간다)
#3. 전체 누적합에서 없앨부분 두 곳을 빼고, 겹친 부분을 더한다 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
#N크기에 담아둘 숫자
arr = []
for i in range(N):
    li = list(map(int, input().split()))
    arr.append(li)

dp = [[0]*(N+1) for _ in range(N+1)]


#누적합 구하기 
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

#M줄에 걸친 위치에 함수를 적용해 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int ,input().split())
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
#N크기에 담아둘 숫자
arr = []
for i in range(N):
    li = list(map(int, input().split()))
    arr.append(li)

#구간합
def sum_num(x1, y1, x2, y2):
    count = 0
    #범위 주의 -> 인덱스때문에 -1씩 빼준다다
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            count += arr[i][j]
    return count

#M줄에 걸친 위치에 함수를 적용해 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int ,input().split())
    result = sum_num(x1, y1, x2,y2)
    print(result)


##### 누적합 다른 풀이
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + arr[i-1][j-1]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j]

