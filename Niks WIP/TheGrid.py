class SmallGrid:
	def __init__(self, vertical=5, horizontal=5, doors =[], gridNumber=0):
		#Initialize should create the gridworld environment and accept an array of terminal states.
		self.x = horizontal
		self.y = vertical
		self.gridNumber = gridNumber
		self.doors = doors
		
		self.grid = [0] * self.x
		for i in range(self.x):
			self.grid[i] = [0] * self.y
			
	
	def makeYourMove(self, move, playerX, playerY, probability):
		#up
		if move == 1:
			if probability != 2:
				playerY += -1
				if probability == 3:
					playerX += -1
				if probability == 4:
					playerX += 1
		#down
		elif move == 2:
			if probability != 2:
				playerY += 1
				if probability == 3:
					playerX += 1
				if probability == 4:
					playerX += -1
		#Right
		elif move == 3:
			if probability != 2:
				playerX += 1
				if probability == 3:
					playerX += -1
				if probability == 4:
					playerX += 1
		#Down
		elif move == 4:
			if probability != 2:
				playerX += -1
				if probability == 3:
					playerY += 1
				if probability == 4:
					playerY += -1
		
		
		#If they go off, reset the incorrect value.
		if playerX < 0: playerX = 0
		if playerX > self.x: playerX = self.x
		if playerY < 0: playerY = 0
		if playerY > self.y: playerY = self.y
		
		return [playerX, playerY]

	def doorCheck(self, playerX, playerY):
		
		
		
	def printOut(self):
		pStr = "\t"
		for i in range(self.x): pStr = pStr + "____" 
		pStr = pStr + "_\n"
		for i in range(self.x):
			pStr = pStr + "\t"
			for j in range(self.y):
				pStr = pStr + "|   "
			pStr = pStr + "|\n\t"
			for j in range(self.y):
				pStr = pStr + "| " + self.grid[i][j] + " "
			pStr = pStr + "|\n\t"
			for j in range(self.y):
				pStr = pStr + "|___"
			pStr = pStr + "|\n"