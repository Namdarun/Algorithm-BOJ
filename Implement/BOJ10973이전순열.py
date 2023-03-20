#BOJ10973_이전순열
#브루트포스로 해결함
N = int(input())
arr = list(map(int, input().split()))

#맨 뒤에서부터 
for i in range(N-1, 0, -1):
    if arr[i-1] > arr[i]:
        for j in range(N-1, 0, -1):
            if arr[i-1] > arr [j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:],reverse=True)
                print(*arr)
                exit()
else: 
    print(-1)


#정석버전 - 런타임에러 
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

#k의 최댓값 찾기
k = -1
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        k = i

if k == -1:
    print(-1)


else:
    for j in range(k+1, len(arr)):
        if arr[j] < arr[i]:
            m = j
            
    arr[k], arr[m] = arr[m], arr[k]

    arr_back = arr[k+1:]
    arr_back.sort(reverse=True)
    result = arr[:k+1] + arr_back

    for k in result:
        print(k, end=' ')
    print()