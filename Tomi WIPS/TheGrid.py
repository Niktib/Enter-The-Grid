import gridAgent

debug = True

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
			
	
	def makeYourMove(self, agent, probability):
		move = agent.move()
		print("pre agent Move: {}, {}".format(move,agent.playerStatus()))
		#up
		if move == 1:
			if probability != 2:
				agent.playerY += -1
				if probability == 3:
					agent.playerX += -1
				if probability == 4:
					agent.playerX += 1
		#down
		elif move == 2:
			if probability != 2:
				agent.playerY += 1
				if probability == 3:
					agent.playerX += 1
				if probability == 4:
					agent.playerX += -1
		#Right
		elif move == 3:
			if probability != 2:
				agent.playerX += 1
				if probability == 3:	
					agent.playerX += -1
				if probability == 4:
					agent.playerX += 1
		#Down
		elif move == 4:
			if probability != 2:
				agent.playerX += -1
				if probability == 3:
					agent.playerY += 1
				if probability == 4:
					agent.playerY += -1
		print("post agent Move: {}, {}".format(move,agent.playerStatus()))
		return self.errorAndDoorCheck(agent)

	def errorAndDoorCheck(self, agent):
		#1 = North, 2 = East, 3 = South, 4 = West
		door = 0
		atDoor = False
		#Did the agent walk through a door? HAs to be in the middle of the array and past the door
		print("Door and Error Check, {}".format(agent.playerStatus())) if debug else False
		if 1 in self.doors and agent.playerY < 0 and agent.playerX + 1 == round(self.x/2):	
			atDoor = True
			door = 1
		elif 2 in self.doors and agent.playerY > self.y-1 and agent.playerX + 1 == round(self.x/2):	
			atDoor = True
			door = 2
		elif 3 in self.doors and agent.playerX < 0 and agent.playerY + 1 == round(self.y/2):	
			atDoor = True
			door = 3
		elif 4 in self.doors and agent.playerX > self.x-1 and agent.playerY + 1 == round(self.y/2):	
			atDoor = True
			door = 4


		#If they go off, reset the incorrect value.
		if agent.playerX < 0: agent.playerX = 0
		if agent.playerX > self.x-1: agent.playerX = self.x-1
		if agent.playerY < 0: agent.playerY = 0
		if agent.playerY > self.y-1: agent.playerY = self.y-1

		return {'atDoor' : atDoor, 'door' : door}


	def printOut(self, agent):
		if agent.currentGrid == self.gridNumber:
			pStr = "\t"
			for i in range(self.x):
				if 1 in self.doors and i == self.x/2:
					continue
				pStr = pStr + "____" 
			pStr = pStr + "_\n"
			for i in range(self.x):
				pStr = pStr + "\t"
				for j in range(self.y):
					pStr = pStr + "|   "
				pStr = pStr + "|\n\t"
				for j in range(self.y):
					pStr = pStr + "| " + str(self.grid[i][j] if not(agent.playerX == j and agent.playerY == i) else "A") + " "
				pStr = pStr + "|\n\t"
				for j in range(self.y):
					pStr = pStr + "|___"
				pStr = pStr + "|\n"
			print(pStr)
		else:	
			pStr = "\t"
			for i in range(self.x): 
				if 1 in self.doors and i == self.x/2:
					continue
				pStr = pStr + "____" 
			pStr = pStr + "_\n"
			for i in range(self.x):
				pStr = pStr + "\t"
				for j in range(self.y):
					pStr = pStr + "|   "
				pStr = pStr + "|\n\t"
				for j in range(self.y):
					pStr = pStr + "| " + str(self.grid[i][j]) + " "
				pStr = pStr + "|\n\t"
				for j in range(self.y):
					pStr = pStr + "|___"
				pStr = pStr + "|\n"
			print(pStr)