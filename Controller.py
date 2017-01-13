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
        while True:
            if refresh:
                response=raw_input("New game? 'Y' or 'N' \n")
                if response[0]=='N' or response[0]=='n':
                    print "Goodbye!"
                    sys.exit()
                elif response[0]=='Y' or response[0]=='y':
                    board=Board(5,5) #improvement:allow players to choose board size
                    refresh=False
                else:
                    print "Please follow the input format"
            else:
                response=raw_input("Type \n 'f [row] [col]' to flag \n 'c [row] [col] to choose' \n 'q' to exit \n")
                if response[0]=='f':
                    
                    #TODO flag
                    print "Flagged"

                elif response[0]=='q':
                    print "Goodbye!"
                    sys.exit()
                elif response[0]=='c':
                    #TODO choose
                    print "Chosen"
                #TODO win boolean
                rows=5
                cols=5
                for r in range(rows):
                    for c in range(cols):
                        print board.listOfRows[r][c].getContent(),
                    print ""

    if __name__=="__main__":
        main()