import random, math
from Cell import Cell

class Board(object):
	"""Represents the Minesweeper board. The game ends when all cells on the board but the mines have been exposed.
	Possible Improvements: timer, threaded leadership board"""
	rows=0
	cols=0
	listOfRows=[] #Contains the cells
	numMines=0
	numRevealed=0

	def __init__(self, rows, cols):
		self.listOfRows=[[Cell(False) for r in range(rows)] for i in range(cols)] #initialize all Cells to 0
		self.rows=rows
		self.cols=cols
		self.numMines=math.ceil(self.rows*self.cols*0.2)
		self.placeMines(self.numMines)
		
		for r in range(rows):
			for c in range(cols):
				minesNearby=self.neighboringMines(r,c)
				self.listOfRows[r][c].updateContent(minesNearby)

	def placeMines(self,numMines):
		#Precondition: numMines >= 0 and <= number of cells on the board. 
		#Postcondition: numMines mines are placed on the board. 
		for i in range(int(numMines)):
			self.placeMine()
	
	def placeMine(self):
		#Places an individual mine.
		row=random.randint(0,self.rows-1)
		col=random.randint(0,self.cols-1)
		while self.listOfRows[row][col].isMine()==True:
			row=random.randint(0,self.rows-1) #row-major
			col=random.randint(0,self.cols-1)
		self.listOfRows[row][col]=Cell(True)
		return True

	def neighboringMines(self,r,c):
		#Returns the number of mines in the 8 neighboring cells.
		number=0
		delRow=[-1,0,1]
		delCol=[-1,0,1]
		for row in delRow:
			for col in delCol:
				if (row+r)>=0 and (row+r)<self.rows and (col+c)>=0 and (col+c)<self.cols and self.listOfRows[row+r][col+c].isMine():
					number+=1
		return number

	def flag(self,r,c):
		self.listOfRows[r][c].playerFlag()

	def unflag(self,r,c):
		self.listOfRows[r][c].playerFlag(False)

	def getContent(self):
		#Returns the player's view of contents of the cells on the board in a 2D array
		playerView=[]
		playerView=[["" for r in range(self.rows)] for i in range(self.cols)] 
		for r in range(self.rows):
			for c in range(self.cols):
				playerView[r][c]=self.listOfRows[r][c].playerGetContent()
		return playerView

	def reveal(self, r, c):
		#Reveals the cell content if it is not a mine
		if self.listOfRows[r][c].isMine():
			return False
		elif self.listOfRows[r][c].number>0:
			if(not self.listOfRows[r][c].revealed):
				self.listOfRows[r][c].playerReveal()
				self.numRevealed+=1
			return True
		else:
			numExposed=self.ripple(r,c)
			self.numRevealed+=numExposed
			return True

	def won(self):
		#Returns true if all the non-mine cells have been revealed
		if (self.numRevealed==self.rows*self.cols-self.numMines):
			return True

	def revealAll(self):
		#Returns all the contents of the cells on the board
		return self.listOfRows

	def ripple(self,r,c):
		#Exposes all blank cells (cells with 0 mines around) and their neighboring number cells
		if not((r)>=0 and (r)<self.rows and (c)>=0 and (c)<self.cols and not self.listOfRows[r][c].isMine()):
			return 0
		if self.listOfRows[r][c].revealed:
			return 0
		#if 0, ripple again
		if self.listOfRows[r][c].number==0:
			return self.listOfRows[r][c].playerReveal()+self.ripple(r-1,c)+self.ripple(r-1,c-1)+self.ripple(r-1,c+1)+self.ripple(r,c-1)+self.ripple(r,c+1)+self.ripple(r+1,c)+self.ripple(r+1,c-1)+self.ripple(r+1,c+1)
		#a number other than 0 and not revealed
		else:
			return self.listOfRows[r][c].playerReveal()
		

