"""take in the user input"""
#improvement: gui

from Board import Board
from Cell import Cell
from View import View 

import sys
class Controller:
    def main():
        refresh=True
        board=None
        while (True):
            """if refresh:
                                                    response=raw_input("New game? 'Y' or 'N' \n")
                                                    if response[0]=='N' or response[0]=='n':
                                                        print "Goodbye!"
                                                        sys.exit()"""
            """"elif response[0]=='Y' or response[0]=='y':"""
            board=Board(5,5) #improvement:allow players to choose board size
            refresh=False
            """else:
                                                                    print "Please follow the input format"""
            if (not board.won()):
                response=raw_input("Type \n 'f [row] [col]' to flag \n 'c [row] [col] to choose' \n 'q' to exit \n")
                if response[0]=='f':
                    r=response[2]
                    c=response[4]
                    board.flag(int(r),int(c))

                elif response[0]=='q':
                    print "Goodbye!"
                    sys.exit()
                elif response[0]=='c':
                    r=response[2]
                    c=response[4]
                    if (not board.reveal(int(r),int(c))):
                        break
                #TODO win boolean
                rows=5
                cols=5
                """for r in range(rows):
                                                                    for c in range(cols):
                                                                        print board.getContent()[r][c],
                                                                    print ''"""

                for r in range(rows):
                    for c in range(cols):
                        print board.listOfRows[r][c].playerGetContent(),
                    print ""
        if (not board.won()):
            for r in range(rows):
                    for c in range(cols):
                        print board.revealAll()[r][c].getContent(),
                    print ""
            print "Kek. You lost. Better luck next time!"
        else:
            print "Congrats, you won!"

    if __name__=="__main__":
        main()