
class Cell:
	"""Represents an individual cell on the Minesweeper board. 
	Is either a number representing the number of neighboring mines or a mine. 
	The content displayed to the player will be different from the actual content if it has not been revealed yet."""

	mine=False
	number=0
	flagged=False #flagged by player
	revealed=False #chosen or revealed by player

	#If mine is true, the cell holds a mine
	def __init__(self,mine=True):
		self.mine=mine
	
	#Returns whether or not the cell contains a mine
	def isMine(self):
		return self.mine

	#Returns the actual content of the cell
	def getContent(self):
		if self.mine==True:
			return "M"
		else:
			return self.number
	#Updates the content of the cell to be the number of neighboring mines. Only for cells that do not contain mines
	def updateContent(self,neighboringMines):
		self.number=neighboringMines

	#Returns the player's view of the content of the cell
	def playerGetContent(self):
		if self.flagged==True:
			return "F"
		elif self.revealed==True:
			return self.getContent()
		else:
			return "?"

	#Flags the cell
	def playerFlag(self, flag=True):
		self.flagged=flag
	
	#Reveals the actual content of the cell 
	def playerReveal(self):
		self.flagged=False
		self.revealed=True
		return 1
