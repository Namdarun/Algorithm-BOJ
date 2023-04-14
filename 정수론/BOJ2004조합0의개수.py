#BOJ2004_조합0의개수_S2
#https://www.acmicpc.net/problem/2004

# n M의 끝자리 0의 개수 출력 프로그램
# N은 20억까지라서 일반팩토리얼로 풀면 무조건 시간초과
# 10은 2와 5로 이뤄져있따....?
# 강의 참고함

n, m = map(int, input().split())

#5와 2로 각각 나눠떨어지게
def num(a, b):
    count = 0
    while a:
        a //= b
        count += a
    return count


five = num(n, 5) - num(m, 5) - num(n - m, 5)
two= num(n, 2) - num(m, 2) - num(n - m, 2)

result = min(five, two)
print(result)