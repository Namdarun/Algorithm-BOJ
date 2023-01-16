#BOJ12865_평범한배낭_스까묵기
#dp는 표를 그려보자 / 더 꽉차게 담을 수 있으면 집어넣기
N, K = map(int, input().split())
#bag에 담을 가치
obj = [[0, 0]]
#obj 담을 배낭
bag = [[0] * (K+1) for _ in range(N+1)]

#가치들 입력
for _ in range(N):
    obj.append(list(map(int, input().split())))

#인덱스 주의
for i in range(1, N+1):
    for j in range(1,K+1):
        w = obj[i][0]
        v = obj[i][1]

        #넣을 무게가 그면 그대로
        if j < w:
            bag[i][j] = bag[i-1][j]

        #무게가 허용된다면 가치중에 더 높은 가치 넣기 
        #최대가치 저장하기
        else:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-w]+v)

print(bag[N][K])
