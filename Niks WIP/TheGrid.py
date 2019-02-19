import random
from datetime import datetime

class GridWorld:
	def __init__(self, vertical=4, horizontal=4, p1=0.8, p2=0.1):
		#Initialize should create the gridworld environment and accept an array of terminal states.
		random.seed(datetime.now())
		self.x = horizontal
		self.y = vertical
		self.p1 = p1
		self.p2 = p2	
		
		self.grid = [None] * self.x
		for i in range(self.y):
			self.board[i] = [None] * self.y
			
	def setTerminal(self, terminal= [[0,0], [self.x, self.y]]):
		#places terminal messages in grid locations assigned
		for i in range(self.x):
			for j in range(self.y):
				if i == terminal[0][0] and j == terminal[0][1]:
					self.board[i][j] = "T"
				else:
					self.board[i][j] = 0
					
	def setRewards(self, rUp, rDown, rLeft, rRight):
		self.rUp = rUp
		self.rDown = rDown
		self.rLeft = rLeft
		self.rRight = rRight
	
	def makeYourMove(self, move, playerX, playerY):
		reward = 0
		probability = randomMovement()
		if move == "Up":
			reward += self.rUp
			if probability != 2:
				playerY += -1
				if probability == 3:
					playerX += -1
				if probability == 4:
					playerX += 1
				
		elif move == "Down":
			reward += self.rDown
			if probability != 2:
				playerY += 1
				if probability == 3:
					playerX += 1
				if probability == 4:
					playerX += -1
				
		elif move == "Right":
			reward += self.rRight
			if probability != 2:
				playerX += 1
				if probability == 3:
					playerX += -1
				if probability == 4:
					playerX += 1
				
		elif move == "Left":
			reward += self.rLeft
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
		
		return [playerX, playerY, reward]
	
	def randomMovement(self):
		result = random.random()
		adjacent = (1 - (self.p1 + self.p2)) / 2
		if result < self.p1:
			#Move correctly
			return 1
		elif result < self.p1 + self.p2:
			#Maintain location
			return 2		
		elif result < self.p1 + self.p2 + adjacent:
			#Counter Clockwise of choice
			return 3		
		else:
			#Clockwise of choice
			return 4
			
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