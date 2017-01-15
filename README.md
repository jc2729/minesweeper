# minesweeper
Based on the classic Windows game (and also my childhood favorite) Minesweeper, this project is a console-based game. The player starts with a 5x5 board and his/her task is to uncover all the cells without mines. The cells are represented by a ?, and the player can flag potential mines, unflag, and reveal cells. The game uses the row-major order. A 3x3 board with [row] [col] would look like this:

(0,0) (0,1) (0,2) <br>
(1,0) (1,1) (1,2) <br>
(2,0) (2,1) (2,2)

When a player reveals a cell, if the cell is a mine, the player loses; otherwise, the cell contains a number conveying the number of the 8 neighboring cells containing mines. I made one addition to the game, allowing players to request hints, revealing cell(s) on the board.
