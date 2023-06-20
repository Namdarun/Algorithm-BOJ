#BOJ20413_MVP다이아몬드_S2
#https://www.acmicpc.net/problem/20413

n = int(input())
s, g, p, d = list(map(int, input().split()))
grade = input()
sum = 0
prev = 0

#n만큼 돌면서 전달, 이번달 과금액에 sum
# prev는 최대과금액으로 초기화
for i in range(n):
    if grade[i] == 'B':
        sum += s - 1 - prev
        prev = s - 1 - prev
    elif grade[i] == 'S':
        sum += g - 1 - prev
        prev = g - 1 - prev
    elif grade[i] == 'G':
        sum += p - 1 - prev
        prev = p - 1 - prev
    elif grade[i] == 'P':
        sum += d - 1 - prev
        prev = d - 1 - prev
    elif grade[i] == 'D':
        sum += d
        prev = d
        
print(sum)
