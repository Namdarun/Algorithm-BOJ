#nonBOJ15702_중간고사채점
N, M = map(int, input().split())
score = list(map(int, input().split()))
arr = []
result = []
for i in range(M):  
    info = list(map(str, input().split()))
    arr.append(info)
    num = int(info[0])
    count = 0
    for j in range(1, len(score)+1):
        if arr[i][j] == 'O':
            count += score[j-1]
        elif arr[i][j] == 'X':
            continue
    
    result.append([num, count])

result.sort(key=lambda result: (-result[-1], result[0]) )
print(result[0][0], result[0][1])