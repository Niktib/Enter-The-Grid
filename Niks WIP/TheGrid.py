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

		return self.errorAndDoorCheck(playerX, playerY)

	def errorAndDoorCheck(self, playerX, playerY):
		#1 = North, 2 = East, 3 = South, 4 = West
		door = 0
		atDoor = False
		#Did the agent walk through a door? HAs to be in the middle of the array and past the door
		if 1 in self.doors and playerY < 0 and playerX + 1 == round(self.x/2):	
			atDoor = True
			door = 1
		elif 2 in self.doors and playerY > self.y-1 and playerX + 1 == round(self.x/2):	
			atDoor = True
			door = 2
		elif 3 in self.doors and playerX < 0 and playerY + 1 == round(self.y/2):	
			atDoor = True
			door = 3
		elif 4 in self.doors and playerX > self.x-1 and playerY + 1 == round(self.y/2):	
			atDoor = True
			door = 4


		#If they go off, reset the incorrect value.
		if playerX < 0: playerX = 0
		if playerX > self.x-1: playerX = self.x-1
		if playerY < 0: playerY = 0
		if playerY > self.y-1: playerY = self.y-1

		return [playerX, playerY, atDoor, door]


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