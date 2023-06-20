#BOJ19949_영재의 시험_S2
#https://www.acmicpc.net/problem/19949

# 5지선다 객관식 10문제 range 1~6, 문제들의 정답이 10개 주어짐
# 3개의 연속된 문제 답은 같지 않다 -> 5개 이상 맞추는 경우 
# 백트래킹으로 풀자

#내 답, 맞춘 갯수, 
def backtracking(mine, solution_count, check):
    global count, solutions
    
    # 10문제 모두 푼 경우
    if check == 10:  
        # 정답이 5문제 이상인 경우
        if solution_count >= 5:  
            count += 1
        return 

    # 10문제 풀기 이전
    not_answer = 0
    if check >= 2 and mine[check - 1] == mine[check - 2]:
        not_answer = mine[check - 1]

    for i in range(1, 6):  # 5지선다 (1, 2, 3, 4, 5)
        # 연속으로 같은 답이면 넘어가기
        if i == not_answer:  
            continue
        mine[check] = i
        # 정답인 경우
        if solutions[check] == i:  
            backtracking(mine, solution_count + 1, check + 1)
        # 오답인 경우
        else:  
            backtracking(mine, solution_count, check + 1)
        mine[check] = 0  # 백트래킹: 현재 문제의 정답 초기화


solutions = list(map(int, input().split()))
count = 0
#백트래킹 함수로 가자
backtracking([0] * 10, 0, 0)
print(count)