"""take in the user input"""
#improvement: gui

from Board import Board
from Cell import Cell

import sys
class Controller:
    def main():
        refresh=True
        board=None
        board=Board(5,5) 

        while (True):
       
            if (not board.won()):
                response=raw_input("Type \n 'f [row] [col]' to flag \n 'u [row] [col]' to unflag \n 'c [row] [col] to choose' \n 'q' to exit \n")
                if response[0]=='f': #flag
                    r=response[2]
                    c=response[4]
                    board.flag(int(r),int(c))
                elif response[0]=='u': #unflag
                    r=response[2]
                    c=response[4]
                    board.unflag(int(r),int(c))
                elif response[0]=='q':
                    print "Goodbye!"
                    sys.exit()
                elif response[0]=='c':  
                    r=response[2]
                    c=response[4]
                    if (not board.reveal(int(r),int(c))):
                        break
                rows=5
                cols=5
                for r in range(rows):
                    
                    for c in range(cols):
                        print board.getContent()[r][c],
                    print ""
                for r in range(rows):
                    
                    for c in range(cols):
                        print board.listOfRows[r][c].getContent(),
                    print ""

        if (not board.won()):
            for r in range(self.rows):
                    for c in range(self.cols):
                        print board.revealAll()[r][c].getContent(),
                    print ""
            print "You lost. Better luck next time!"
        else:
            print "Congrats, you won!"

    if __name__=="__main__":
        main()