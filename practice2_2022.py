row,column=map(int,input().split(' '))
correct=[[0 for i in range(column)] for j in range(row)]
simulate=[[0 for i in range(column)] for j in range(row)]
for i in range(column):
    correct[i] = input().split(' ')
for i in range(column):
    for j in range(row):
        correct[i][j]=int(correct[i][j])

end=True


while end:
    Rcomplete=[ ]
    Ccomplete=[ ]
    cnt=0
    for i in range(column):
        for j in range(row):
            if correct[i][j]==0:
                cnt+=1
    if cnt==(row)*(column):
        end=False

    for i in range(column):
        store=correct[i][0]
        cnt=0
        for j in range(row):
            if store == 0 or store == correct[i][j]:
                cnt+=1
            store = correct[i][j]
        if cnt == column:
            Ccomplete.append(j)

    for i in range(row):
        store=correct[i][0]
        cnt=0
        for j in range(column):
            if store == 0 or store == correct[j][i]:
                cnt+=1
            store = correct[j][i]
        if cnt == row:
            Rcomplete.append(j)

    if len(Rcomplete) == 0 and len(Ccomplete) == 0:
        end=False
    else:
        for i in Rcomplete:
            print('H',str(i),str(correct[i][0]))
            for j in range(column):
                correct[i][j]=0

        for i in Ccomplete:
            print('V',str(i),str(correct[0][i]))
            for j in range(column):
                correct[j][i]=0