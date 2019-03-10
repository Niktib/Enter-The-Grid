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
		#1 = North, 2 = East, 3 = South, 4 = West

		#up
		if move == agent.North:
			if probability != 2:
				agent.playerY += -1
				if probability == 3:
					agent.playerX += -1
				if probability == 4:
					agent.playerX += 1
		#down
		elif move == agent.South:
			if probability != 2:
				agent.playerY += 1
				if probability == 3:
					agent.playerX += 1
				if probability == 4:
					agent.playerX += -1
		#Right
		elif move == agent.East:
			if probability != 2:
				agent.playerX += 1
				if probability == 3:	
					agent.playerX += -1
				if probability == 4:
					agent.playerX += 1
		#Down
		elif move == agent.West:
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
		print("Door and Error Check, {}, round(self.x): {}".format(agent.playerStatus(),round(self.x))) if debug else False #debug
		if (1 in self.doors) and (agent.playerY < 0) and (agent.playerX == round(self.x/2)):	
			atDoor = True
			door = 1
		elif 2 in self.doors and agent.playerX == self.x and agent.playerY  == round(self.x/2):	
			atDoor = True
			door = 2
		elif 3 in self.doors and agent.playerX == round(self.x/2) and agent.playerY  == self.y:	
			atDoor = True
			door = 3
		elif 4 in self.doors and agent.playerX < 0 and agent.playerY  == round(self.y/2):	
			atDoor = True
			door = 4

		print("end errorCheck atDoor: {}, door: {}, (conditions: {}), self.door: {}, self.gridNum: {}".format(atDoor,door,(2 in self.doors),self.doors, self.gridNumber )) if debug else False #debug
		#If they go off, reset the incorrect value.
		if agent.playerX < 0: agent.playerX = 0
		if agent.playerX > self.x-1: agent.playerX = self.x-1
		if agent.playerY < 0: agent.playerY = 0
		if agent.playerY > self.y-1: agent.playerY = self.y-1
		return {'atDoor' : atDoor, 'door' : door}


	def printOut(self, agent, goal):
		if agent.currentGrid == self.gridNumber:
			pStr = "\t"
			for i in range(self.x):
				if 1 in self.doors and i == int(self.x/2):
					pStr = pStr + "     " 
				else:
					pStr = pStr + "____" 
					pass
			pStr = pStr + "_\n"
			for i in range(self.x):
				pStr = pStr + "\t"
				for j in range(self.y):
					pStr = pStr + "|   "
				pStr = pStr + "|\n\t"
				for j in range(self.y):
					if agent.playerX == j and agent.playerY == i:
						pStr = pStr + "| " + "A" + " "
					elif goal['grid'] == self.gridNumber and goal['x'] == j and goal['y'] == i:
						pStr = pStr + "| " + "G" + " "
					else:
						pStr = pStr + "| " + str(self.grid[i][j]) + " "
				pStr = pStr + "|\n\t"
				# to open but door at the bottom
				for j in range(self.y):
					if i == int(self.y-1) and 3 in self.doors and j == int(self.x/2):
						pStr = pStr + "|   "
					else:
						pStr = pStr + "|___"
				pStr = pStr + "|\n"
			print(pStr)

		#if player not on grid 
		else:	
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
				if 4 in self.doors and i == self.x-1:
					pStr = pStr + "\t"
					for j in range(self.y):
						if j == int(self.y/2):
							pStr = pStr + "|   "
						else:
							pStr = pStr + "|   "
					pStr = pStr + "|\n\t"
					for j in range(self.y):
						pStr = pStr + "| " + str(self.grid[i][j]) + " "
					pStr = pStr + "|\n\t"
					for j in range(self.y):
						pStr = pStr + "|___"
					pStr = pStr + "|\n"

				else:
					pStr = pStr + "\t"
					for j in range(self.y):
						pStr = pStr + "|   "
					pStr = pStr + "|\n\t"
					for j in range(self.y):
						pStr = pStr + "| " + str(self.grid[i][j]) + " "
					pStr = pStr + "|\n\t"
					# to open but door at the bottom
					for j in range(self.y):
						if i == int(self.y-1) and 3 in self.doors and j == int(self.x/2):
							pStr = pStr + "|   "
						else:
							pStr = pStr + "|___"
					pStr = pStr + "|\n"
			print(pStr)