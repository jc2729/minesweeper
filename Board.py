#improvement: timer, threaded leadership board

import random, math
from Cell import Cell

class Board(object):
	rows=0
	cols=0
	listOfRows=[]
	numMines=0
	numRevealed=0
	def __init__(self, rows, cols):

		#initialize all Cells to 0
		self.listOfRows=[[Cell(False) for r in range(rows)] for i in range(cols)] 
		self.rows=rows
		self.cols=cols
		self.numMines=math.ceil(self.rows*self.cols*0.2)
		self.placeMines(self.numMines)
		
		for r in range(rows):
			for c in range(cols):
				minesNearby=self.neighboringMines(r,c)
				#correct output
				self.listOfRows[r][c].updateContent(minesNearby)

	def placeMines(self,numMines):
		#maximum number of mines
		for i in range(int(numMines)):
			self.placeMine()
	
	def placeMine(self):
		row=random.randint(0,self.rows-1)
		col=random.randint(0,self.cols-1)
		#Places an individual mine
		while self.listOfRows[row][col].isMine()==True:
			row=random.randint(0,self.rows-1) #row-major
			col=random.randint(0,self.cols-1)
		self.listOfRows[row][col]=Cell(True)
		return True

	def neighboringMines(self,r,c):
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
		playerView=[]
		playerView=[["" for r in range(self.rows)] for i in range(self.cols)] 
		for r in range(self.rows):
			for c in range(self.cols):
				playerView[r][c]=self.listOfRows[r][c].playerGetContent()
		return playerView

	def reveal(self, r, c):
		if self.listOfRows[r][c].isMine():
			return False
		elif self.listOfRows[r][c].number>0:
			self.listOfRows[r][c].playerReveal()
			self.numRevealed+=1
			print self.numRevealed
			return True
		else:

			self.listOfRows[r][c].playerReveal()
			print self.numRevealed
			numExposed=self.ripple(r,c)
			print numExposed
			assert numExposed!=-1
			self.numRevealed+=numExposed
			return True

	def won(self):
		if (self.numRevealed==self.rows*self.cols-self.numMines):
			return True

	def revealAll(self):
		return self.listOfRows

#THIS IS WRONG KMS
	def ripple(self,r,c):
		delRow=[-1,0,1]
		delCol=[-1,0,1]
		for row in delRow:
			for col in delCol:
				if (row+r)>=0 and (row+r)<self.rows and (col+c)>=0 and (col+c)<self.cols and not self.listOfRows[row+r][col+c].isMine():
					if self.listOfRows[row+r][col+c].number==0:
						return 1+self.ripple(row+r,col+c)
					return self.listOfRows[r][c].playerReveal()
		return -1
