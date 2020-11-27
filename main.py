def MakeField(Bombs, Size, Num):
    field = [[0 for i in range(Size)] for j in range(Size)]
    print(Size)
    for i in range(Num):
        print(i)
        field[Bombs[i][0]][Bombs[i][1]] = 'B'

    for i in range(Size):
        for j in range(Size):
            if(field[i][j] != 'B'):
                if(i-1)>=0:
                    if(field[i-1][j]=='B'):
                        field[i][j]+=1
                if(j-1)>=0:
                    if(field[i][j-1]=='B'):
                        field[i][j]+=1
                if(i-1)>=0 and (j-1)>=0:
                    if(field[i-1][j-1]=='B'):
                        field[i][j]+=1
                if(i+1)<Size:
                    if(field[i+1][j]=='B'):
                        field[i][j]+=1
                if(j+1)<Size:
                    if(field[i][j+1]=='B'):
                        field[i][j]+=1
                if(j+1)<Size and (i+1)<Size:
                    if(field[i+1][j+1]=='B'):
                        field[i][j]+=1
                if(i-1)>=0 and (j+1)<Size:
                    if(field[i-1][j+1]=='B'):
                        field[i][j]+=1
                if(i+1)<Size and (j-1)>=0:
                    if(field[i+1][j-1]=='B'):
                        field[i][j]+=1  
    return field

def ShowSolved(Field):
    print('+',end='')
    for i in range((len(Field)*2)):
        print('-',end='')
    print('+')
    for i in range(len(Field)):
        print('|', end='')
        for j in range(len(Field)):
            if Field[i][j] == 0:
                print('.', end=' ')
            else:
                print(Field[i][j], end=' ')
        print('|')
    print('+',end='')
    for i in range((len(Field)*2)):
        print('-',end='')
    print('+')

size = int(input())
n_bombs = int(input())
coord = []
for i in range(n_bombs):
    point = input().split()
    coord.append([int(j) for j in point])

field = MakeField(coord, size, n_bombs)
ShowSolved(field)
