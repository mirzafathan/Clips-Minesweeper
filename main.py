import clips
import game_functions as Game

def Action(str):
    act = str[1]
    print(act)
    if(act == 'o'):
        x = int(str[6])
        print('open work')
        y = int(str[8])
        Game.Open(x, y, field, opened, marked)
    elif(act == 'm'):
        x = int(str[6])
        y = int(str[8])
        Game.Mark(x, y, field, opened, marked)
        Predict.append([x,y])

def UpdateFact():
    for i in range(Size):
        for j in range(Size):
            if (opened[i][j]):
                Fact = '(box (P ' + str(i) + ' ' + str(j)
                if(field[i][j]=='B'):
                    print('You Lose')
                elif (checked[i][j] == False):
                    Fact += ') (safety TRUE) (number '
                    Fact += str(field[i][j])
                    Fact += ') (marked FALSE) (neighboring FALSE))'
                    Temp.append(Fact)
                    checked[i][j] = True
            else:
                Fact = '(box (P ' + str(i) + ' ' + str(j)
                Fact += ') (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))'
                Temp.append(Fact)
            if (marked[i][j]):
                Fact = '(box (P ' + str(i) + ' ' + str(j) + ') (safety FALSE) (number 10) (marked TRUE) (neighboring FALSE))'
                Temp.append(Fact)
    Game.ShowGameField(field, opened, marked)

def Initiate():
    env.load('kbagent.clp')
    env.reset()
    for i in range(-1, Size+1):
        initframe = '(box (P ' + str(-1) + ' ' + str(i) + ') (safety TRUE) (number 0) (marked FALSE) (neighboring FALSE))'
        env.assert_string(initframe)
    for i in range(0, Size+1):
        initframe = '(box (P ' + str(i) + ' ' + str(-1) + ') (safety TRUE) (number 0) (marked FALSE) (neighboring FALSE))'
        env.assert_string(initframe)
    for i in range(0, Size+1):
        initframe = '(box (P ' + str(Size) + ' ' + str(i) + ') (safety TRUE) (number 0) (marked FALSE) (neighboring FALSE))'
        env.assert_string(initframe)
    for i in range(0, Size):
        initframe = '(box (P ' + str(i) + ' ' + str(Size) + ') (safety TRUE) (number 0) (marked FALSE) (neighboring FALSE))'
        env.assert_string(initframe)
    for i in range(Size):
        for j in range(Size):
            initframe = '(box (P ' + str(i) + ' ' + str(j) + ') (safety FALSE) (number 0) (marked FALSE) (neighboring FALSE))'
            env.assert_string(initframe)

def ReInitiate():
    env.clear()
    env.load('kbagent.clp')
    env.reset()
    for i in range(-1, Size+1):
        initframe = '(box (P ' + str(-1) + ' ' + str(i) + ') (safety TRUE) (number 0) (marked FALSE) (neighboring FALSE))'
        env.assert_string(initframe)
    for i in range(0, Size+1):
        initframe = '(box (P ' + str(i) + ' ' + str(-1) + ') (safety TRUE) (number 0) (marked FALSE) (neighboring FALSE))'
        env.assert_string(initframe)
    for i in range(0, Size+1):
        initframe = '(box (P ' + str(Size) + ' ' + str(i) + ') (safety TRUE) (number 0) (marked FALSE) (neighboring FALSE))'
        env.assert_string(initframe)
    for i in range(0, Size):
        initframe = '(box (P ' + str(i) + ' ' + str(Size) + ') (safety TRUE) (number 0) (marked FALSE) (neighboring FALSE))'
        env.assert_string(initframe)
    for i in range(len(Temp)):
        env.assert_string(Temp[i])
    env.run()

if __name__ == "__main__":
    input_method = input('1. Manual\n2. From file\nSelect input method: ')
    input_method = int(input_method)

    # Size = int(input('Masukkan Ukuran:'))
    # Num = int(input('Masukkan Jumlah Bom:'))
    Coord = []
    Predict = []
    Size = 0
    Num = 0
    if input_method == 1:
        Size = int(input("Enter size : "))
        Num = int(input("How many bombs? :"))

        for i in range(Num):
            point = input("Bomb Coordinate : ").split()
            Coord.append([int(j) for j in point])

    elif input_method == 2:
        filename = input('File name: ')
        found = False
        try:
            with open(filename, 'r') as f:
                Size = int(f.readline())
                Num = int(f.readline())

                for i in range(Num):
                    point = f.readline().split()
                    Coord.append([int(j) for j in point])
                f.close()
        except :
            print('[INPUT ERROR] file not found, shutting down')
            quit()

    else:
        print("[INPUT ERROR] input method not valid, shutting down")
        quit()


    # for i in range(n_bombs):
    #     point = input("Bomb Coordinate : ").split()
    #     Coord.append([int(j) for j in point])

    field = Game.MakeField(Coord, Size, Num)
    opened = [[False for i in range(Size)] for j in range(Size)]
    marked = [[False for i in range(Size)] for j in range(Size)]
    checked = [[False for i in range(Size)] for j in range(Size)]
    Temp = []

    Game.ShowGameField(field, opened, marked)

    env = clips.Environment()
    Initiate()
    Action('(open 0 0)')
    UpdateFact()

    ReInitiate()

    for i in env.facts():
        print(i)
  #  UpdateFact()
   # NextMove = 0
    #for i in env.facts():
     #   print(i)