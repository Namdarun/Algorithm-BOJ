#BOJ1244_스위치켜고끄기
s = int(input())
onoff = list(map(int, input().split()))
N = int(input())
for i in range(N):
    hakseng = list(map(int, input().split()))
    #남학생
    if hakseng[0] == 1:
        #남학생 숫자
        x = hakseng[1]
        for j in range(x-1, s):
            if (j+1) % x == 0:
                if onoff[j] == 1:
                    onoff[j] = 0
                else:
                    onoff[j] = 1

    #여학생
    else:
        #여학생 숫자 
        y = hakseng[1]
        #좌우 대칭 범위 명시
        ran = 1
        if onoff[y-1] == 1:
            onoff[y-1] = 0
        else: 
            onoff[y-1] = 1

        while True:
            #범위를 벗어나면 중지 
            if y-1+ran == s or y-1-ran == -1:
                break
            
            #범위안에서 좌우가 대칭일 때 
            elif onoff[y-1+ran] == onoff[y-1-ran]:
                #변경해주기 
                if onoff[y-1+ran] == 1:
                    onoff[y-1+ran] = 0
                    onoff[y-1-ran] = 0

                else:
                    onoff[y-1+ran] = 1
                    onoff[y-1-ran] = 1
                #최대범위가 될때까지 변경해주면 된다.   
                ran += 1
            else:
                break

for i in range(s//20 +1):
    print(*onoff[:20])
    onoff = onoff[20:]