#BOJ2511_카드놀이_B2
#https://www.acmicpc.net/problem/2511

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a == b:
    print(10, 10)
    print('D')
else:
    a_cnt = b_cnt = 0
    for i in range(10):
        if a[i] > b[i]:
            a_cnt += 3; win = 'A'
        elif a[i] < b[i]:
            b_cnt += 3; win = 'B'
        else:
            a_cnt += 1; b_cnt += 1

    print(a_cnt, b_cnt)
    if a_cnt == b_cnt:
        print(win)
    else:
        print('A' if a_cnt > b_cnt else 'B')
    