#BOJ10816_숫자카드2_S4
# https://www.acmicpc.net/problem/10816

#몰랐는데 이게 해시알고리즘 이라고 한다 

n = int(input())
n_num = list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

# cnt에 저장 후 key가 존재하면 개수 반환, 그 외엔 0 반환 
cnt ={}
for i in n_num:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in m_num:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')