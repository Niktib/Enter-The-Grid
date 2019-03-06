import random
from datetime import datetime
from TheGrid import SmallGrid

class GridWorld:
	def __init__(self, vertical=5, horizontal=5, p1=0.8, p2=0.1, numOfGrids=4):
		#Initialize should create the gridworld environment and accept an array of terminal states.
		random.seed(datetime.now())
		self.p1 = p1
		self.p2 = p2
		self.reward = -1
		self.currentGrid = 1

		self.arrayOfGrids = []
		for i in range(numOfGrids) -1:
			self.arrayOfGrids.append(SmallGrid(vertical,horizontal,[i, i+1], i))
		self.arrayOfGrids.append(SmallGrid(vertical,horizontal,[4, 1], 4))
		'''
		Grids are connected: 
		1 has a north(Grid 2) and east door (grid 4)
		2 has a south(Grid 1) and east door (grid 3)
		3 has a south(Grid 4) and west door (grid 2)
		4 has a north(Grid 3) and west door (grid 1)
		'''

	def agentMove(self, move, playerX, playerY, currentGrid):
		#Results= [playerX, playerY, atDoor (True or false), Cardinal direction of door]
		#1 = North, 2 = East, 3 = South, 4 = West
		results = self.arrayOfGrids[currentGrid].makeYourMove(move, playerX, playerY, self.randomMovement())
		
		

		return [results[0], results[1], self.reward, currentGrid]
	
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

	def pieceItTogether(self):
		'''
		1. Take a grid, iterate through the list adding future grids to possible connecting doors.
		2. Check if there any non-used doors, 
			a. if so go back to step one
			b. If this process has been repeated X times, or there are no other iterations, randomly pick one iteration.
		3. If any doors are un-used, remove them from the grids.
		'''