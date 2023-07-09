N,M = map(int, input().split(' '))
valid=True
list_tis=[[None for k in range(3)] for j in range(M)]       #로그 별 tis
#start_and_end=[[None for k in range(2)] for j in range(N)]  #유저 별 시작,종료
for j in range(M):
    t,i,s = map(int, input().split(' '))
    list_tis[j][0]=t
    list_tis[j][1]=i
    list_tis[j][2]=s


for k in range(1,N+1):
    bef_time=0
    bef_status=1
    for j in range(M):
        if list_tis[j][1]==k:
            if bef_status==list_tis[j][2]:
                valid=False
            else:
                bef_status=list_tis[j][2]
            if (list_tis[j][0]-bef_time>=60) or (bef_time==0):
                bef_time=list_tis[j][0]
            else:
                valid=False
        if not valid:
            break
    if bef_status == 0:
        valid=False
    if valid==False:
        break

if valid==False:
    print('NO')
else:
    print('yes')
