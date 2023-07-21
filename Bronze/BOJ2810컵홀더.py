#BOJ2810_컵홀더_B1
#https://www.acmicpc.net/problem/2810

n = int(input())
form = input()

cnt = form.count("LL")

if cnt <= 1:
    print(len(form))

else:
    print(len(form) - cnt + 1)