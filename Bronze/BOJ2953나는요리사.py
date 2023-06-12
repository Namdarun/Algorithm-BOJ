#BOJ2953_나는요리사_B3
#https://www.acmicpc.net/problem/2953

total = []
for _ in range(5):
    score = list(map(int, input().split()))
    total.append(sum(score))
print(total.index(max(total)) + 1, max(total))