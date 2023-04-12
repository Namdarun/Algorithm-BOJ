#BOJ2004_조합0의개수_S2
#https://www.acmicpc.net/problem/2004

# N M의 끝자리 0의 개수 출력 프로그램
# N은 20억까지라서 일반팩토리얼로 풀면 무조건 시간초과
# 10은 2와 5로 이뤄져있따....?

N, M = map(int, input().split())

def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


five_count = count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5)
two_count = count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)

answer = min(five_count, two_count)
print(answer)