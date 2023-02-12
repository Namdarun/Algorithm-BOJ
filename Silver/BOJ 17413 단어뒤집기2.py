#BOJ17413_단어뒤집기2.py
#https://www.acmicpc.net/problem/17413

import sys
input = sys.stdin.readline
s = input().rstrip()
check = False
word = ""
ans = ""

for i in s:
    if check == False:
        if i == "<":
            check = True
            word += i
        elif i == " ":
            word += i
            ans += word
            word = ""
        else:
            word = i + word


    else:
        word += i
        if i == ">":
            check = False
            ans += word
            word = ""

print(ans + word)

