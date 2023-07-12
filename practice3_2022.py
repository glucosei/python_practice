N,M = map(int, input().split(' '))
lst_map=[]
for i in range(N):
    lst_map.append(list(map(int,input().split(' '))))

sum_water=[]
#십자 모양
for i in range(N):
    for j in range(N):
        store=0
        #lst_map[i][j]가 물풍선 터트릴 위치
        #가로
        start=j-M
        end=j+M+1
        if j+M>=N:
            end=N
        if j-M<=0:
            start=0
        #모기잡기
        for k in range(start,end):
            store+=lst_map[i][k]
        
        #세로
        start=i-M
        end=i+M+1
        if i+M>=N:
            end=N
        if i-M<=0:
            start=0
        #모기잡기
        for k in range(start,end):
            store+=lst_map[k][j]
        
        store-=lst_map[i][j]
        sum_water.append(store)
        

#엑스 자 모양
for i in range(N):
    for j in range(N):
        store=0
        #lst_map[i][j]가 물풍선 터트릴 위치
        #왼쪽 위
        for k in range(M+1):
            if i-k>=0 and j-k>=0:
                try:
                    store+=lst_map[i-k][j-k]
                except IndexError:
                    pass
        
        #왼쪽 아래
        for k in range(M+1):
            if i+k>=0 and j-k>=0:
                try:
                    store+=lst_map[i+k][j-k]
                except IndexError:
                    pass

        #오른쪽 위
        for k in range(M+1):
            if i-k>=0 and j+k>=0:
                try:
                    store+=lst_map[i-k][j+k]
                except IndexError:
                    pass
        
        #오른쪽 아래
        for k in range(M+1):
            if i+k>=0 and j+k>=0:
                try:
                    store+=lst_map[i+k][j+k]
                except IndexError:
                    pass

        store-=lst_map[i][j]*3
        sum_water.append(store)
        
        
       
print(max(sum_water))
