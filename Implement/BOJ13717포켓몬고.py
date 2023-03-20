#BOJ13717_포켓몬GO
#풀이법에 대한 충격...
N = int(input())
total = 0
max_num = 0
for i in range(N):
    P = input()
    K, M = map(int, input().split())
    cnt = 0
    #빼고 2 더하고 cnt에 1 더하기
    while K <= M:
        M -= K
        M += 2
        cnt += 1
    #결과값 다 더해주기
    total += cnt 

    #최댓값 찾기 -> 최댓값에 맞는 몬스터 도출
    #똑같아도 앞부터 보기때문에 몬스터가 도출된다.
    if cnt > max_num:
        max_num = cnt
        max_name = P

print(total)
print(max_name)