import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import platform
import os
from colorama import Fore, Back, Style 
from main import consts

def main():
    
    gamefield = [[0 for i in range(consts.GAME_SIZE)] for j in range(consts.GAME_SIZE)] 

    # gamefield = [[],[]]
    for i in range(8):
        for j in range(8):
            if (i % 2 == 0):
                if (j % 2 == 0):
                    gamefield[i][j]="◼"
                else:
                    gamefield[i][j]="◻"
            else:
                if (j % 2 == 0):
                    gamefield[i][j]="◻"
                else:
                    gamefield[i][j]="◼"
    for k in range(8):
        gamefield[1][k] ="♙"   
        gamefield[6][k] ="♟"

    __runGame = True
    while __runGame:
        clear()
        __printMenu()
        __printGame(gamefield)
        __printFooter()
        __runGame=__getInput()

def __printMenu():
    print("\t\tNeues Spiel(N)\t\tSpeichern(S)\tLaden(L)\t\tSpiel Beenden(B)")
    print("\t\t________________________________________________________________________________")

def __printFooter():
    print("\t\t________________________________________________________________________________")   

def __printGame(gamefield):
    print("\n\t\t\t\t    A    B    C    D    E    F    G    H\n")
    __printGameLine(gamefield,7)
    __printGameLine(gamefield,6)
    __printGameLine(gamefield,5)
    __printGameLine(gamefield,4)
    __printGameLine(gamefield,3)
    __printGameLine(gamefield,2)
    __printGameLine(gamefield,1)
    __printGameLine(gamefield,0)
    print("\n\t\t\t\t    A    B    C    D    E    F    G    H")

def __printGameLine(gamefield,lineNumber):
    print("\t\t\t       ",end="")
    print(str(lineNumber+1)+"",end="")
    print("    "+str(gamefield[lineNumber][0])+"",end="")
    print("    "+str(gamefield[lineNumber][1])+"",end="")
    print("    "+str(gamefield[lineNumber][2])+"",end="")
    print("    "+str(gamefield[lineNumber][3])+"",end="")
    print("    "+str(gamefield[lineNumber][4])+"",end="")
    print("    "+str(gamefield[lineNumber][5])+"",end="")
    print("    "+str(gamefield[lineNumber][6])+"",end="")
    print("    "+str(gamefield[lineNumber][7])+"",end="")
    print("     "+str(lineNumber+1))

def __getInput():
    print("\t\t\t\tBitte Menü Aktion eingeben oder Bauer wählen")
    desiccion = input("\t\t\t\t")
    desiccion = str.upper(desiccion)

    if desiccion == consts.LOAD:
        print("\t\t\t\tSpiel Laden")
        return True
    elif desiccion == consts.SAVE:
        print("\t\t\t\tSpiel Speichern ...")
        return True
    elif desiccion == consts.NEW_GAME:
        print("\t\t\t\tNeues Spiel")
        return True
    elif desiccion == consts.QUIT:
        return __quitGame()
    else:
        return True


def __quitGame():
    clear()
    os.system('color 0F')
    return False
    
if(platform.system() == "Windows"):
    clear = lambda: os.system("cls")
    os.system('color F0')
elif(platform.system == "Linux"):
    clear = lambda: os.system('clear') 
    os.system('setterm -background white -foreground white -store') 

if __name__ == "__main__":
    main()
    