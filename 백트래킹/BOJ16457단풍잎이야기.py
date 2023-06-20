#BOJ16457_단풍잎이야기_S1
#https://www.acmicpc.net/problem/16457

# 라가가 싸이코패쓰네 일퀘 못 참는데...
# 최대로 깰 수 있는 퀘스트의 개수
# n은 10 이하 스킬이름은 1~20까지의 정수
# 최대 20개 중에 n개를 골라서 m*k


# k를 잘못 이해하고 있었다. = 퀘스트당 사용해야하는 스킬의 개수
# k개씩 m개의 퀘스트가 나오는 것이고, n개의 키보드를 적절히 배치해 4개 중 최대의 개수를 구하는 것
# 조합을 이용해서 푼다...못외움

n, m, k = map(int, input().split())
skill = [list(map(int, input().split())) for _ in range(m)]
selected = [0] * n
answer = 0

def recur(cur, start):  # 조합 -> mCn -> m! / (m - n)! / n!
    #조합 만들기, n개 다 뽑았으면 
    if cur == n:
        #중복 제거
        check = set(selected)
        cnt = 0
        for i in skill:
            for j in i:
                if j not in check:
                    break
            else:
                cnt += 1   
    
        #최댓값을 갱신
        global answer
        if cnt > answer:
            answer = cnt
        return
    
    #1부터 시작하므로 start+1*로 가야함?
    for i in range(start+1, 2*n+1):
        selected[cur] = i
        # 재귀
        recur(cur+1, i)
        
recur(0, 0)
print(answer)

# ## 조합
# n, m = map(int, input().split())
# selected = [0] * n
# def recur(cur, start):  # 조합 -> mCn -> m! / (m - n)! / n!
#     if cur == n:
#         print(*selected)
#         return
#     for i in range(start, m):
#         selected[cur] = i
#         recur(cur + 1, i + 1)
# recur(0, 0)