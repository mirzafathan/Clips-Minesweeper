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

def ShowField(Field):
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

def ShowGameField(Field, Done):
    print('+',end='')
    for i in range((len(Field)*2)):
        print('-',end='')
    print('+')
    for i in range(len(Field)):
        print('|', end='')
        for j in range(len(Field)):
            if Field[i][j] == 0:
                if opened[i][j]:
                    print(' ', end=' ')
                else:
                    print('.', end=' ')
            else:
                if opened[i][j]:
                    print(Field[i][j], end=' ')
                else:
                    print('.', end=' ')
        print('|')
    print('+',end='')
    for i in range((len(Field)*2)):
        print('-',end='')
    print('+')


def open(x, y):
    if not opened[x][y]:
        if(field[x][y]!='B'):
            if(field[x][y]==0):
                opened[x][y]=True
                if(x>0) and (y>0):
                    open(x-1,y-1)
                if(x>0):
                    open(x-1,y)
                if(x>0) and (y<size-1):
                    open(x-1,y+1)
                if(y>0):
                    open(x,y-1)
                if(y<size-1):
                    open(x,y+1)
                if(x<size-1) and (y>0):
                    open(x+1,y-1)
                if(x<size-1):
                    open(x+1,y)
                if(x<size-1) and (y<size-1):
                    open(x+1,y+1)
            else:
                opened[x][y]=True
        else:
            opened[x][y]=True
            print("You Open a Bomb. You Lose.")
        ShowGameField(field, opened)

size = int(input())
n_bombs = int(input())
coord = []
for i in range(n_bombs):
    point = input().split()
    coord.append([int(j) for j in point])

field = MakeField(coord, size, n_bombs)
opened = [[False for i in range(size)] for j in range (size)]

ShowGameField(field, opened)
open(0,0)
ShowField(field)
#ShowSolved(field)