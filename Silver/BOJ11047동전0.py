#BOJ11047_동전0 
#입력
N, K = map(int, input().split())
arr = []
for i in range(N):
    value = int(input())
    arr.append(value)

#내림차순으로 변경 후 큰 값으로 나눠지면 몫을 동전개수에 추가 
#나누지 못하면 다음 값으로 이동
arr.sort(reverse=True)
count = 0
while K > 0:
    if arr[0] > K:
        arr.pop(0)
    else:
        count += K//arr[0]
        K = K%arr[0]

print(count)