#nonBOJ15702_중간고사채점
#딕셔너리로 하는 법 깨우치자 
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
            result.append((num, count))
        elif arr[i][j] == 'X':
            continue

mv = 0
ans = []
for i in result:
    if i > mv:
        mv = i
        ans.append(mv)
print(ans)