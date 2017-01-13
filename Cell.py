
class Cell:
	mine=False
	number=0
	flagged=False
	revealed=False

	def __init__(self):
		print "hola"
	def __init__(self,mine=True):
		self.mine=mine
	
	def isMine(self):
		return self.mine

	def getContent(self):
		if self.mine==True:
			return "M"
		else:
			return self.number
	
	def updateContent(self,neighboringMines):
		self.number=neighboringMines

	def playerGetContent(self):
		if self.flagged==True:
			return "F"
		elif self.revealed==True:
			return self.getContent()
		else:
			return "?"

	def playerFlag(self, flag=True):
		self.flagged=flag
	
	def playerReveal(self):
		self.flagged=False
		self.revealed=True
		return 1
