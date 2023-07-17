#주어진 수열에서 가장 큰 합을 구하는 함수
def get_max(subject):
    log=[ ]
    length = len(subject)
    for i in range(length):
        for j in range(i,length):
            log.append(sum(subject[i:j+1]))
    return max(log)


#뒤집는 함수
def reverse(subject):
    length=len(subject)
    log = [ ]
    for i in range(length):
        for j in range(length):
            if i <= j:
                store=subject[i:j+1]
                store.reverse()
                lst_reverse=lst[:i]+store+lst[j+1:]
            else:
                store=subject[j:i+1]
                store.reverse()
                lst_reverse=lst[:j]+store+lst[i+1:]
                log.append(get_max(lst_reverse))
    return max(log)


#메인
num = int(input())
lst = list(map(int, input().split(' ')))
print(reverse(lst))