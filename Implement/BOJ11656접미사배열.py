#BOJ11656_접미사배열_S4
#https://www.acmicpc.net/problem/11656

word = input()
check = []

for i in range(len(word)):
    check.append(word[i:])

check.sort()

for i in check:
    print(i)