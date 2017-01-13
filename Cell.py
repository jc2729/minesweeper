#mines around it
#hence its display
#receives information only about mines around it

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
