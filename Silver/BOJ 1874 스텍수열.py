#BOJ1874_스택수열_S2
#https://www.acmicpc.net/problem/1874

n = int(input())
stack = []
answer = []
check = 0
plus = 1
#n 수만큼 입력
for i in range(n):
    num = int(input())
    # 입력한 수를 만날 때 까지 오름차순으로 push
    while plus <= num:       
        stack.append(plus)
        answer.append("+")
        plus += 1

    # 입력한 수를 만나면 while문 탈출. 즉 plus = num일 때 까지 while문을 돌아 스택을 쌓는다.
    #스택의 탑이 입력숫자와 같다면 - 추가
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    #스택의 탑이 입력숫자가 아니면 스텍 쌓는게 불가
    #NO 출력하고 1로 초기화 후 탈출
    else:          
        print("NO")   
        check = 1             
        break               

if check == 0:
    for i in answer:
        print(i)

