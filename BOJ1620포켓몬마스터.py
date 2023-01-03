#BOJ1620_포켓몬마스터
N, M = map(int, input().split())
N_list = []
M_list = []
for i in range(N):
    N_list.append(input())
    
for j in range(M):
    M_list.append(input())

result = []
for i in range(len(M_list)):
    #알파벳이면 해당 단어 인덱스 도출
    if M_list[i].isalpha():
        result.append(N_list.index(M_list[i])+1)
    
    #숫자면 해당 인덱스에 맞는 단어 도출
    elif M_list[i].isdigit():
        result.append(N_list[int(M_list[i])-1])

    else:
        break

for i in result:
    print(i)