import random
from datetime import datetime
from TheGrid import SmallGrid

debug = True

class GridWorld:
	def __init__(self, agent=None, vertical=5, horizontal=5, p1=0.8, p2=0.1, numOfGrids=4):
		#Initialize should create the gridworld environment and accept an array of terminal states.
		random.seed(datetime.now())
		self.p1 = p1
		self.p2 = p2
		self.reward = -1
		self.currentGrid = 1
		self.map = dict()
		self.agent = agent
		self.arrayOfGrids = []
		self.goal = {"grid": 2, "x" : 2 , "y" : 2}
		for i in range(1,numOfGrids):
			self.arrayOfGrids.append(SmallGrid(vertical,horizontal,[i, i+1], i))
		self.arrayOfGrids.append(SmallGrid(vertical,horizontal,[4, 1], 4))
		'''
		Grids are connected: 
		1 has a north(Grid 2) and east door (grid 4)
		2 has a south(Grid 1) and east door (grid 3)
		3 has a south(Grid 4) and west door (grid 2)
		4 has a north(Grid 3) and west door (grid 1)
		'''

	def insertAgent(self,agent):
		self.agent = agent

	def agentMove(self):
		#Results= { 'atDoor' : atDoor (True or false), 'door' : Cardinal direction of door}
		#1 = North, 2 = East, 3 = South, 4 = West
		results = self.arrayOfGrids[self.agent.currentGrid-1].makeYourMove(self.agent, 1)
		if (self.agent.currentGrid == self.goal['grid'] and self.agent.playerX == self.goal['x'] and self.agent.playerY == self.goal['y']):
			self.agent.reward += 100
			return
		if results['atDoor']:
			print("At Door: Grid: {}, Direction: {}".format(self.agent.currentGrid,results['door']))
			self.agent.currentGrid = self.map[self.agent.currentGrid][results['door']]
			if results['door'] == 1:
				self.agent.playerY = self.arrayOfGrids[self.agent.currentGrid-1].y-1
			elif results['door'] == 2:
				self.agent.playerX = 0
			elif results['door'] == 3:
				self.agent.playerX = int(self.arrayOfGrids[self.agent.currentGrid-1].x/2)
				self.agent.playerY = 0
			elif results['door'] == 4:
				self.agent.playerY = int(self.arrayOfGrids[self.agent.currentGrid-1].y/2)
				self.agent.playerX = int(self.arrayOfGrids[self.agent.currentGrid-1].x-1)
			self.agent.reward += self.reward
		else:
			self.agent.reward += self.reward
	
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
		#1 = North, 2 = East, 3 = South, 4 = West
		mapBasic = {self.arrayOfGrids[i].gridNumber: dict() for i in range(len(self.arrayOfGrids))}
		#keep  a 'map' of the layout so indexing in self.map[currentGrid][cardinal of door] retuns connected grid
		for i in mapBasic:
			mapBasic[i] = {self.arrayOfGrids[i-1].doors[d]: 0 for d in range(len(self.arrayOfGrids[i-1].doors)) }
		
		# Hard code the door connections for now 
		mapBasic[1][1] = 2
		mapBasic[1][2] = 4

		mapBasic[2][2] = 3
		mapBasic[2][3] = 1

		mapBasic[3][3] = 4
		mapBasic[3][4] = 2

		mapBasic[4][1] = 3
		mapBasic[4][4] = 1

		self.map = mapBasic
		print("Basic Map: {}".format(self.map)) if debug else False #debug variable at top of file 
	
	def printOut(self):
		print("Grid World Printout: {}".format(self.arrayOfGrids))	
		for grid in self.arrayOfGrids:
			#for now only print agent current grid
			if True:# grid.gridNumber == self.agent.currentGrid:
				print("Grid #: {}, gridDoors: {}".format(grid.gridNumber,grid.doors)) if debug else False #debug
				grid.printOut(self.agent, self.goal)
				# Possibly make grid print out return string, and use map to put ones connected to each other in correct order
				# then use new line to make next line of grid lower and append string 