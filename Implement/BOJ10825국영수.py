#BOJ10825_국영수_S4
#https://www.acmicpc.net/problem/10825

#람다를 쓰면 편하게 풀 수 있다.

n = int(input())
student = []

for _ in range(n):
    student.append(input().split())

#국영수 점수를 int로 변환 후 크기에 맞춰서 정렬
student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    #n갯수만큼 돌면서 student의 이름들 출력(정렬마침)
    print(student[i][0])