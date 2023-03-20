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
        elif arr[i][j] == 'X':
            continue
        result.append([num, count])
        
min_i , max_j = 100001 , 0 
for i, j in result:
    if max_j < j:
        max_j = j
        if min_i > i:
            min_i = i

print(i, end=' ')
print(j)
        