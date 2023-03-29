#BOJ11719 입력대로출력_B3
#https://www.acmicpc.net/problem/11719

# EOFError = 파일의 시작과 끝 
#에러가 발생하면 멈추고, 아니면 입력받은대로 출력
while(True):
    try:
        print(input())
    except EOFError:
        break