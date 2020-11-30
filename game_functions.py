def MakeField(Bombs, Size, Num):
    field = [[0 for i in range(Size)] for j in range(Size)]
    for i in range(Num):
        field[Bombs[i][0]][Bombs[i][1]] = 'B'

    for i in range(Size):
        for j in range(Size):
            if(field[i][j] != 'B'):
                if(i-1) >= 0:
                    if(field[i-1][j] == 'B'):
                        field[i][j] += 1
                if(j-1) >= 0:
                    if(field[i][j-1] == 'B'):
                        field[i][j] += 1
                if(i-1) >= 0 and (j-1) >= 0:
                    if(field[i-1][j-1] == 'B'):
                        field[i][j] += 1
                if(i+1) < Size:
                    if(field[i+1][j] == 'B'):
                        field[i][j] += 1
                if(j+1) < Size:
                    if(field[i][j+1] == 'B'):
                        field[i][j] += 1
                if(j+1) < Size and (i+1) < Size:
                    if(field[i+1][j+1] == 'B'):
                        field[i][j] += 1
                if(i-1) >= 0 and (j+1) < Size:
                    if(field[i-1][j+1] == 'B'):
                        field[i][j] += 1
                if(i+1) < Size and (j-1) >= 0:
                    if(field[i+1][j-1] == 'B'):
                        field[i][j] += 1
    return field


def ShowField(Field):
    print('+', end='')
    for i in range((len(Field)*2)):
        print('-', end='')
    print('+')
    for i in range(len(Field)):
        print('|', end='')
        for j in range(len(Field)):
            if Field[i][j] == 0:
                print('.', end=' ')
            else:
                print(Field[i][j], end=' ')
        print('|')
    print('+', end='')
    for i in range((len(Field)*2)):
        print('-', end='')
    print('+')


def ShowGameField(Field, Done, Flag):
    print('+', end='')
    for i in range((len(Field)*2)):
        print('-', end='')
    print('+')
    for i in range(len(Field)):
        print('|', end='')
        for j in range(len(Field)):
            if Field[i][j] == 0:
                if Done[i][j]:
                    print(' ', end=' ')
                elif Flag[i][j]:
                    print('M', end=' ')
                else:
                    print('.', end=' ')
            else:
                if Done[i][j]:
                    print(Field[i][j], end=' ')
                elif Flag[i][j]:
                    print('M', end=' ')
                else:
                    print('.', end=' ')
        print('|')
    print('+', end='')
    for i in range((len(Field)*2)):
        print('-', end='')
    print('+')


def Open(x, y, field, opened, marked):
    size = len(field)
    if not opened[x][y]:
        if(field[x][y] != 'B'):
            if(field[x][y] == 0):
                opened[x][y] = True
                if(x > 0) and (y > 0):
                    Open(x-1, y-1, field, opened, marked)
                if(x > 0):
                    Open(x-1, y, field, opened, marked)
                if(x > 0) and (y < size-1):
                    Open(x-1, y+1, field, opened, marked)
                if(y > 0):
                    Open(x, y-1, field, opened, marked)
                if(y < size-1):
                    Open(x, y+1, field, opened, marked)
                if(x < size-1) and (y > 0):
                    Open(x+1, y-1, field, opened, marked)
                if(x < size-1):
                    Open(x+1, y, field, opened, marked)
                if(x < size-1) and (y < size-1):
                    Open(x+1, y+1, field, opened, marked)
            else:
                opened[x][y] = True
        else:
            opened[x][y] = True
            print("You Open a Bomb. You Lose.")
        ShowGameField(field, opened, marked)


def Mark(x, y, field, opened, marked):
    if not marked[x][y]:
        marked[x][y] = True
        ShowGameField(field, opened, marked)


"""
size = int(input())
n_bombs = int(input())
coord = []
for i in range(n_bombs):
    point = input().split()
    coord.append([int(j) for j in point])

field = MakeField(coord, size, n_bombs)
opened = [[False for i in range(size)] for j in range (size)]
marked = [[False for i in range(size)] for j in range (size)]


Tester
Uncomment to Test

ShowGameField(field, opened, marked)
i = input().split()
i = [int(j) for j in i]
while i[0]!=100:
    m = input("mark or open? ")
    if(m=='o'):
        Open(i[0],i[1])
    else:
        Mark(i[0],i[1])
    i = input().split()
    i = [int(j) for j in i]
ShowField(field)
"""
