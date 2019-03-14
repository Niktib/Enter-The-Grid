debug = False

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
		
	def makeYourMove(self, playerX, playerY, move, probability):
		#1 = North, 2 = East, 3 = South, 4 = West

		#up
		if move == 1:
			if probability != 2:
				playerY += -1
				if probability == 3:
					playerX += -1
				if probability == 4:
					playerX += 1
		#Right
		elif move == 2:
			if probability != 2:
				playerX += 1
				if probability == 3:	
					playerX += -1
				if probability == 4:
					playerX += 1
		#down
		elif move == 3:
			if probability != 2:
				playerY += 1
				if probability == 3:
					playerX += 1
				if probability == 4:
					playerX += -1
		#left
		elif move == 4:
			if probability != 2:
				playerX += -1
				if probability == 3:
					playerY += 1
				if probability == 4:
					playerY += -1
		return self.errorAndDoorCheck(playerX, playerY)

	def dimensionsOfGrid(self):
		return [self.x, self.y]
		
	def errorAndDoorCheck(self, playerX, playerY):
		#1 = North, 2 = East, 3 = South, 4 = West
		door = 0
		atDoor = False
		#Did the agent walk through a door? HAs to be in the middle of the array and past the door
		if (1 in self.doors) and (playerY < 0) and (playerX == round(self.x/2)):	
			atDoor = True
			door = 1
		elif 2 in self.doors and playerX == self.x and playerY  == round(self.x/2):	
			atDoor = True
			door = 2
		elif 3 in self.doors and playerX == round(self.x/2) and playerY  == self.y:	
			atDoor = True
			door = 3
		elif 4 in self.doors and playerX < 0 and playerY  == round(self.y/2):	
			atDoor = True
			door = 4

		print("end errorCheck atDoor: {}, door: {}, self.door: {}, self.gridNum: {}".format(atDoor,door,self.doors, self.gridNumber )) if debug else False #debug
		#If they go off, reset the incorrect value.
		if playerX < 0: playerX = 0
		if playerX > self.x-1: playerX = self.x-1
		if playerY < 0: playerY = 0
		if playerY > self.y-1: playerY = self.y-1
		return {'atDoor' : atDoor, 'door' : door, 'playerX' : playerX, 'playerY' : playerY}


	def printOut(self, playerPos, goal):
		pStr = "\t"
		for i in range(self.x):
			print("printOut i: {} , self.x/2: {}, self.x: {}".format(i,self.x/2,self.x)) if False else False
			if 1 in self.doors and i == int(self.x/2):
				pStr = pStr + "     " 
			else:
				pStr = pStr + "____" 
				pass
		pStr = pStr + "_\n"
		for i in range(self.x):
			if 2 in self.doors and i == int(self.x/2):
				pStr = pStr + "\t"
				for j in range(self.y):
					pStr = pStr + "|   "
				pStr = pStr + "\n\t"
				for j in range(self.y):
					if playerPos[0] == j and playerPos[1] == i and self.gridNumber == playerPos[2]:
						pStr = pStr + "| " + "A" + " "
					elif goal['grid'] == self.gridNumber and goal['x'] == j and goal['y'] == i:
						pStr = pStr + "| " + "G" + " "
					else:
						pStr = pStr + "| " + ' ' + " "
				pStr = pStr + "\n\t"
				for j in range(self.y):
					pStr = pStr + "|___"
				pStr = pStr + "\n"
			elif 4 in self.doors and i == int(self.x/2):
				pStr = pStr + "\t"
				for j in range(self.y):
					if j == 0:
						pStr = pStr + "    "
					else:
						pStr = pStr + "|   "
				pStr = pStr + "|\n\t"
				for j in range(self.y):
					if j == 0:
						if playerPos[0] == j and playerPos[1] == i and self.gridNumber == playerPos[2]:
							pStr = pStr + "  " + "A" + " "
						elif goal['grid'] == self.gridNumber and goal['x'] == j and goal['y'] == i:
							pStr = pStr + "  " + "G" + " "
						else:
							pStr = pStr + "  "+ ' ' + " "
					else:
						if playerPos[0] == j and playerPos[1] == i and self.gridNumber == playerPos[2]:
							pStr = pStr + "| " + "A" + " "
						elif goal['grid'] == self.gridNumber and goal['x'] == j and goal['y'] == i:
							pStr = pStr + "| " + "G" + " "
						else:
							pStr = pStr + "| " + ' ' + " "
				pStr = pStr + "|\n\t"
				for j in range(self.y):
					if j == 0:
						pStr = pStr + " ___"
					else:
						pStr = pStr + "|___"
				pStr = pStr + "|\n"
			else:
				pStr = pStr + "\t"
				for j in range(self.y):
					pStr = pStr + "|   "
				pStr = pStr + "|\n\t"
				for j in range(self.y):
					if playerPos[0] == j and playerPos[1] == i and self.gridNumber == playerPos[2]:
						pStr = pStr + "| " + "A" + " "
					elif goal['grid'] == self.gridNumber and goal['x'] == j and goal['y'] == i:
						pStr = pStr + "| " + "G" + " "
					else:
						pStr = pStr + "| " + ' ' + " "
				pStr = pStr + "|\n\t"
				# to open but door at the bottom
				for j in range(self.y):
					if i == int(self.y-1) and 3 in self.doors and j == int(self.x/2):
						pStr = pStr + "|   "
					else:
						pStr = pStr + "|___"
				pStr = pStr + "|\n"
		print(pStr)