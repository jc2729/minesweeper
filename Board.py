#improvement: timer, threaded leadership board
#placemines()
#getmines()
#display/print number of mines
#revealcells() randomly
import random, math
from Cell import Cell

class Board(object):
	rows=0
	cols=0
	listOfRows=[]
	numMines=0
	kek=False
	def __init__(self, rows, cols):

		#initialize all Cells to 0
		self.listOfRows=[[Cell(False) for r in range(rows)] for i in range(cols)] 
		self.rows=rows
		self.cols=cols
		self.kek=True
		self.numMines=math.ceil(self.rows*self.cols*0.2)
		self.placeMines(self.numMines)
		
		for r in range(rows):
			for c in range(cols):
				minesNearby=self.neighboringMines(r,c)
				#correct output
				self.listOfRows[r][c].updateContent(minesNearby)
				print self.listOfRows[r][c].getContent(),

	def placeMines(self,numMines):
		#maximum number of mines
		for i in range(int(numMines)):
			self.placeMine()
	
	def placeMine(self):
		row=random.randint(0,self.rows-1)
		col=random.randint(0,self.cols-1)
		#Places an individual mine
		while self.listOfRows[row][col].isMine()==True:
			row=random.randint(0,self.rows-1) #rows are vertical
			col=random.randint(0,self.cols-1)
		self.listOfRows[row][col]=Cell(True)
		#print "asamine at" + str((row, col))
		return True

	def neighboringMines(self,r,c):
		number=0
		delRow=[-1,0,1]
		delCol=[-1,0,1]
		#print (r, c)
		for row in delRow:
			for col in delCol:
				if (row+r)>=0 and (row+r)<self.rows and (col+c)>=0 and (col+c)<self.cols and self.listOfRows[row+r][col+c].isMine():
					#print "mine at" + str((row+r, col+c))
					number+=1
		#print number
		return number
