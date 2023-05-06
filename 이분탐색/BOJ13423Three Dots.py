#BOJ13423_Three Dots_S2
#https://www.acmicpc.net/problem/13423
import sys
input = sys.stdin.readline

#cased 안에서의 수를 넣고, 이분탐색을 해가고 조건에 맞으면 cnt를 세준다 

n = int(input())
for _ in range(n):
    case = int(input())
    case_num = list(map(int, input().split()))

    cnt = 0
    for i in range(case-1):
        for j in range(i+1, case):
            if (case_num[i] + case_num[j]) % 2 == 0 and (case_num[i] + case_num[j]) // 2 in case_num:
                cnt += 1

    print(cnt) 