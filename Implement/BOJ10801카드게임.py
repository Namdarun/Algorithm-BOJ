#BOJ10801_카드게임_B2
#https://www.acmicpc.net/problem/10801

card1 = list(map(int,input().split()))
card2 = list(map(int,input().split()))
a,b = 0,0
for i in range(10):
    if card1[i] > card2[i]:
        a+=1
    elif card1[i] < card2[i]:
        b+=1

if a>b:
    print('A')
elif a<b:
    print("B")
else:
    print("D")