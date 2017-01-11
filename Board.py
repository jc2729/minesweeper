#improvement: timer, threaded leadership board
#placemines()
#getmines()
#display/print number of mines
#revealcells() randomly
import random
from Cell import Cell

class Board(object):
	def __init__(self, rows, cols):

		#initialize all Cells to 0
		listOfRows=[[Cell()]*rows for i in range(cols)] 

		"""for r in range(rows):
			for c in range(cols):
				print listOfRows[r][c]"""

