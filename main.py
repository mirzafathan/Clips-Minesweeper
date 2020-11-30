import game_functions as Game

input_method = input('1. Manual\n2. From file\nSelect input method: ')
input_method = int(input_method)

size = 0
n_bombs = 0
coord = []

if input_method == 1:
    size = int(input("Enter size : "))
    n_bombs = int(input("How many bombs? :"))

    for i in range(n_bombs):
        point = input("Bomb Coordinate : ").split()
        coord.append([int(j) for j in point])

elif input_method == 2:
    filename = input('File name: ')
    found = False
    try:
        with open(filename, 'r') as f:
            size = int(f.readline())
            n_bombs = int(f.readline())

            for i in range(n_bombs):
                point = f.readline().split()
                coord.append([int(j) for j in point])
            f.close()
    except :
        print('[INPUT ERROR] file not found, shutting down')
        quit()

else:
    print("[INPUT ERROR] input method not valid, shutting down")
    quit()

field = Game.MakeField(coord, size, n_bombs)
opened = [[False for i in range(size)] for j in range(size)]
marked = [[False for i in range(size)] for j in range(size)]


Game.ShowGameField(field, opened, marked)

i = Game.inputCoordinate()

while i[0] != 100:
    m = input("mark or open? (m/o) ")
    try :
        if(m == 'o'):
            if (Game.Open(i[0], i[1], field, opened, marked)):
                print("Game Field :")
                Game.ShowField()
        else:
            Game.Mark(i[0], i[1], field, opened, marked)

    except:
        print("[ERROR] Input out of range")
    
    if not(Game.ShowGameField(field, opened, marked)):
        print("Game over, you won")
        quit()
    
    i = Game.inputCoordinate()

