#BOJ2775_부녀회장이 될테야
T = int(input())

for _ in range(T):  
    K = int(input())  # 층
    n = int(input())  # 호
    floor = [x for x in range(1, n+1)]  # 0층 리스트
    for k in range(K):  # 층 수 만큼 반복
        for i in range(1, n):  # 1 ~ n-1까지 (인덱스로 사용)
            floor[i] += floor[i-1]  # 층별 각 호실의 사람 수를 변경
        # print(floor)
    print(floor[-1])  # 가장 마지막 수 출력