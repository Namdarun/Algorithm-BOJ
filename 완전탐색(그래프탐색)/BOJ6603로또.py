#BOJ6603_로또_S2
#https://www.acmicpc.net/problem/6603

#라이브러리 사용

import itertools

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    s = arr[1:]

    for i in itertools.combinations(s, 6):
        print(*i)

    if k == 0:
        break
    print()