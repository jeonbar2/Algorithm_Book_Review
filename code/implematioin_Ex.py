
def implementation_1():
    N = int(input())
    x, y = 1, 1
    plans = input().split()

    move_x = [1, -1, 0, 0]
    move_y = [0, 0, 1, -1]
    dir = ['L', 'R', 'U', 'D']

    for i in range(len(plans)):
        if plans[i] == 'L':
            if y - 1 >= 1:
                y -= 1
        elif plans[i] == 'R':
            if y + 1 <= N:
                y += 1
        elif plans[i] == 'U':
            if x - 1 >= 1:
                x -= 1
        elif plans[i] == 'D':
            if x + 1 <= N:
                x += 1
    print(x, y)

    return

def implementation_2():
    N=int(input())
    answer=0
    for i in range(N+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    answer+=1

    print(answer)
    return

def arabian_night():
    answer=0
    input_data=input()
    row= int(input_data[1])
    column = int(ord(input_data[0]))-int(ord('a'))+1  
    if column+2<=8:
        if row+1<=8:
            answer+=1
        if row-1>=1:
            answer += 1
    if column-2>=1:
        if row+1<=8:
            answer+=1
        if row-1>=1:
            answer += 1
    if row+2<=8:
        if column+1<=8:
            answer+=1
        if column-1>=1:
            answer += 1
    if row -2>=1:
        if column+1<=8:
            answer+=1
        if column-1>=1:
            answer += 1
    print(answer)
    return answer
arabian_night()