import game_functions as Game

size = int(input())
n_bombs = int(input())
coord = []
for i in range(n_bombs):
    point = input().split()
    coord.append([int(j) for j in point])

field = Game.MakeField(coord, size, n_bombs)
opened = [[False for i in range(size)] for j in range (size)]
marked = [[False for i in range(size)] for j in range (size)]


Game.ShowGameField(field, opened, marked)
i = input().split()
i = [int(j) for j in i]
while i[0]!=100:
    m = input("mark or open? ")
    if(m=='o'):
        Game.Open(i[0],i[1], field, opened, marked)
    else:
        Game.Mark(i[0],i[1], field, opened, marked)
    i = input().split()
    i = [int(j) for j in i]
Game.ShowField(field)
