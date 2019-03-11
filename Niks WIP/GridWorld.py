import random
from datetime import datetime
from TheGrid import SmallGrid
import time
debug = True

class GridWorld:
	def __init__(self, start, goal, vertical=5, horizontal=5, p1=0.8, p2=0.1, numOfGrids=4):
		#Initialize should create the gridworld environment and accept an array of terminal states.
		random.seed(datetime.now())
		self.p1 = p1
		self.p2 = p2
		self.reward = -1
		self.map = dict()
		self.arrayOfGrids = []
		self.startPoint = start
		self.goal = goal
		self.finished = False
		self.vertical = vertical
		self.horizontal = horizontal
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
		
	def understandingState(self):
		#returns an array with the dimensions for each grid in the grids numbered slot
		gridMap = []
		for i in range(1,numOfGrids):
			gridMap.add(self.arrayOfGrids[i].dimensionsOfGrid())
		return gridMap

	def agentMove(self, playerPos, move):
		#Results= { 'atDoor' : atDoor (True or false), 'door' : Cardinal direction of door}
		#1 = North, 2 = East, 3 = South, 4 = West
		results = self.arrayOfGrids[playerPos[2]-1].makeYourMove(playerPos[0], playerPos[1],  move, randomMovement)
		if (playerPos[2] == self.goal['grid'] and playerPos[0] == self.goal['x'] and playerPos[1] == self.goal['y']):
			reward = 100
			self.finished = True
			return [results['playerPos[0]'], results['playerPos[1]'], reward]
		if results['atDoor']:
			print("At Door: Grid: {}, Direction: {}".format(playerPos[2],results['door']))
			playerPos[2] = self.map[playerPos[2]][results['door']]
			if results['door'] == 1:
				playerPos[1] = self.arrayOfGrids[playerPos[2]-1].y-1
			elif results['door'] == 2:
				playerPos[0] = 0
			elif results['door'] == 3:
				playerPos[0] = int(self.arrayOfGrids[playerPos[2]-1].x/2)
				playerPos[1] = 0
			elif results['door'] == 4:
				playerPos[1] = int(self.arrayOfGridsplayerPos[2]-1].y/2)
				playerPos[0] = int(self.arrayOfGrids[playerPos[2]-1].x-1)
			reward = self.reward
		else:
			reward = self.reward
		return [results['playerPos[0]'], results['playerPos[1]'], reward]
			
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
		#keep  a 'map' of the layout so indexing in self.map[playerPos[2]][cardinal of door] retuns connected grid
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
	
	def printOut(self, playerPos, animate=False):
		print("Grid World Printout: {}".format(self.arrayOfGrids))	
		for grid in self.arrayOfGrids:
			#for now only print agent current grid
			if grid.gridNumber == playerPos[2]:
				print("Grid #: {}, gridDoors: {}".format(grid.gridNumber,grid.doors)) if debug else False #debug
				grid.printOut(playerPos[0], playerPos[1], playerPos[2] self.goal)
				time.sleep(1) if animate else False
				# Possibly make grid print out return string, and use map to put ones connected to each other in correct order
				# then use new line to make next line of grid lower and append string 