num = int(input())
lst = []
lst_parts=[[ ] for i in range(5)]


for i in range(num):
    lst.append(list(input().split(' ')))

#파츠별로 리스트에 분배
for i in range(num):
    store = lst[i]
    if store[0] == 'Body':
        lst_parts[0].append(store)
        lst_parts[0][-1][0] = i
    elif store[0] == 'Handle':
        lst_parts[1].append(store)
        lst_parts[1][-1][0] = i
    elif store[0] == 'Wheel':
        lst_parts[2].append(store)
        lst_parts[2][-1][0] = i
    elif store[0] == 'Engine':
        lst_parts[3].append(store)
        lst_parts[3][-1][0] = i
    else:
        lst_parts[4].append(store)
        lst_parts[4][-1][0] = i

one,lst, two = zip(*lst)
num = int(input())
lst_synergy=[ ]
for i in range(num):
    lst_synergy.append(list(input().split(' ')))
    lst_synergy[i][0] = lst.index(lst_synergy[i][0])
    lst_synergy[i][1] = lst.index(lst_synergy[i][1])
    

goal=int(input())

#다 돌려가면서 최적 찾기 
log = [[],[]]
for i in range(len(lst_parts[0])):
    for j in range(len(lst_parts[1])):
        for k in range(len(lst_parts[2])):
            for l in range(len(lst_parts[3])):
                for m in range(len(lst_parts[4])):
                    log[0].append(str(i)+' '+str(j)+' '+str(k)+' '+str(l)+' '+str(m))
                    score = (int(lst_parts[0][i][2])+int(lst_parts[1][j][2])+int(lst_parts[2][k][2])+int(lst_parts[3][l][2])+int(lst_parts[4][m][2]))
                    for n in lst_synergy:
                        subject = [int(lst_parts[0][i][2]),int(lst_parts[1][j][2]),int(lst_parts[2][k][2]),int(lst_parts[3][l][2]),int(lst_parts[4][m][2])]
                        if n[0] in subject and n[1] in subject:
                            score+=n[2]
                    log[1].append(abs(goal - score))

min_i = log[1].index(min(log[1]))
index_list = list(map(int,log[0][min_i].split(' ')))
for i in range(5):
    print(lst_parts[i][index_list[i]][1])
