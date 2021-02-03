#3-1 거스름돈 문제
#가장 큰돈으로 거슬러 줘야할동전의 갯수구하기문제
#N이 주어야 할 거스름돈


def greedy_1(n):
    count = 0
    list = [500, 100, 50, 10]

    for coin in list:
        count += n // coin
        n %= coin
    return count

def greedy_2():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    first=data[n-1]
    second=data[n-2]
    answer = 0
    while True:
        for i in range(0,k):
            if m==0:
                break
            answer += first
            m-=1
        if m==0:
            break
        answer+=second
        m-=1

    return answer



def greedy_3():
    answer=0
    n ,m = map(int, input().split())
    for i in range(n):
        data=list(map(int,input().split()))
        min_val=min(data)
        answer=max(answer,min_val)

    return answer

def greedy_4():
    n , k=map(int, input().split())
    answer =0
    while True:
        if n%k==0:
            n/=k
            answer+=1
        else:
            n-=1
            answer+=1

        if n==1:
            break
    return answer

print(greedy_4())