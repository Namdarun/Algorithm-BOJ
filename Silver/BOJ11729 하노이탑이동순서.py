#BOJ11729_하노이탑이동순서_S1
#https://www.acmicpc.net/problem/11729

#하노이탑 이동방식
# 맨밑 원반 빼고 나머지들을 옮기고, 맨 밑 판을 아예 다르곳으로 옮김
# 나머지 원판들을 반복
def hanoi(n,a,b):
    #1일땐 그대로 출력
    if n == 1:
        print(a, b)
        return

    #1,2,3 두는 곳으로 설정 후 재귀(직접 해보기)
    hanoi(n-1, a, 6-a-b)
    print(a,b)
    hanoi(n-1, 6-a-b, b)

n = int(input())
#경우의 수 
print(2**n-1)
#재귀
hanoi(n,1,3)