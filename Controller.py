from Board import Board
from Cell import Cell

import sys
class Controller:
    """Takes in the user input from the command-line.
    Improvement: GUI"""
    def main():
        board=None

        #Pre-set board length
        rows=5
        cols=5
        board=Board(rows,cols) 
        print "There are "+ str(int(board.numMines)) +" mines on this board."
        #Print board for the first time
        for r in range(rows):           
            for c in range(cols):
                print board.getContent()[r][c],
            print ""
        
        while (not board.won()):      
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
            elif response[0]=='c':  #choose
                r=response[2]
                c=response[4]
                if (not board.reveal(int(r),int(c))):
                    break

            #Print the board      
            for r in range(rows):  
                for c in range(cols):
                    print board.getContent()[r][c],
                print ""

        if (not board.won()):
            for r in range(rows):
                    for c in range(cols):
                        print board.revealAll()[r][c].getContent(),
                    print ""
            print "You lost. Better luck next time!"
        else:
            print "Congrats, you won!"

    if __name__=="__main__":
        main()