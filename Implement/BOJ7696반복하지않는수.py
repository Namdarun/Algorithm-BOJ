#BOJ7696_반복하지 않는 수_S4 
#https://www.acmicpc.net/problem/7696


#시간초과.ver
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    # 입력값이 0이면 종료 
    if n == 0:
        break

    #숫자
    num = 1

    #숫자의 위치
    index = 0
    #index값이 n과 같아질때까지 계속 num을 오름차순으로 정렬해나간다. 
    while index != n:
        sorting = sorted(list(str(num)))
        ifsame = False

        #중복을 제거했는데, 다르면 중복이 있는 숫자
        if len(sorting) != len(set(sorting)):
            ifsame = True
        
        #같지 않으면 통과
        if not ifsame:
            index += 1

        num += 1
    
    print(num-1)

