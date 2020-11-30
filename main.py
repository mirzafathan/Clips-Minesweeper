import game_functions as Game

input_method = input('1. Manual\n2. From file\nSelect input method: ')
input_method = int(input_method)

size = 0
n_bombs = 0
coord = []

if input_method == 1:
    size = int(input())
    n_bombs = int(input())

    for i in range(n_bombs):
        point = input().split()
        coord.append([int(j) for j in point])
elif input_method == 2:
    filename = input('File name: ')
    with open(filename, 'r') as f:
        size = int(f.readline())
        n_bombs = int(f.readline())

        for i in range(n_bombs):
            point = f.readline().split()
            coord.append([int(j) for j in point])
        f.close()

field = Game.MakeField(coord, size, n_bombs)
opened = [[False for i in range(size)] for j in range(size)]
marked = [[False for i in range(size)] for j in range(size)]


Game.ShowGameField(field, opened, marked)
i = input().split()
i = [int(j) for j in i]
while i[0] != 100:
    m = input("mark or open? ")
    if(m == 'o'):
        Game.Open(i[0], i[1], field, opened, marked)
    else:
        Game.Mark(i[0], i[1], field, opened, marked)
    i = input().split()
    i = [int(j) for j in i]
Game.ShowField(field)
