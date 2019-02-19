
class ValueIteration:
	def __init__(self, rUp, rDown, rLeft, rRight, vertical=4, horizontal=4, p1=0.8, p2=0.1):
		self.rUp = rUp
		self.rDown = rDown
		self.rLeft = rLeft
		self.rRight = rRight
		self.Discount = 0.95
		self.theta = 0.001
		self.p1 = p1
		self.p2 = p2
		
		self.x = horizontal
		self.y = vertical
		self.value = [0] * self.x
		for i in range(self.y):
			self.value[i] = [0] * self.y
			
		self.setTerminal()
			
	def setTerminal(self, terminal= [[0,0], [0,0]]):
		#places terminal messages in grid locations assigned
		self.value[0][0] = "T"
		self.value[self.x-1] [self.y-1] = "T"
					
	def iteration(self, iterate):
		delta = 0
		areWeDoneHere = False
		for runTime in range(iterate):
			for i in range(self.y):
				for j in range(self.x):
					if type(self.value[i][j]) is not str :
						oldValue = self.value[i][j]
						self.value[i][j] = self.bellmanBackup(i, j)
						if self.theta > (oldValue-self.value[i][j]): areWeDoneHere = True
			if areWeDoneHere: break
			print("For Iteration {}:\n".format(runTime+1))
			self.printOut()
		
		print("Final Iteration {}:\n".format(runTime+1))
		self.printOut()
				
	def printOut(self):
		for i in self.value: print(i)
		print("\n")

	def bellmanBackup(self, i, j):
	#j is x-axis, so left is -1 and right is +1
	#i is y-axis, so up is -1 and down is +1
		adjacent = 0.05#(1 - (self.p1 + self.p2)) / 2 
		#Going Up
		action1 = (self.p1 *(self.rUp + self.Discount * self.errorCheck(i-1, j))) + (self.p2 *(self.rUp + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rUp + self.Discount * self.errorCheck(i-1, j+1))) + (adjacent *(self.rUp + self.Discount * self.errorCheck(i-1, j-1)))
		#Going down
		action2 = (self.p1 *(self.rDown + self.Discount * self.errorCheck(i+1, j))) + (self.p2 *(self.rDown + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rDown + self.Discount * self.errorCheck(i+1, j+1))) + (adjacent *(self.rDown + self.Discount * self.errorCheck(i+1, j-1)))
		#Going left
		action3 = (self.p1 *(self.rLeft + self.Discount * self.errorCheck(i, j-1))) + (self.p2 *(self.rLeft + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rLeft + self.Discount * self.errorCheck(i-1, j-1))) + (adjacent *(self.rLeft + self.Discount * self.errorCheck(i+1, j-1)))
		#Going right
		action4 = (self.p1 *(self.rRight + self.Discount * self.errorCheck(i, j+1))) + (self.p2 *(self.rRight + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rRight + self.Discount * self.errorCheck(i-1, j+1))) + (adjacent *(self.rRight + self.Discount * self.errorCheck(i+1, j+1)))
		
		return max([action1, action2, action3, action4])
	
	def errorCheck(self, i, j):
		if i < 0: i = 0
		elif i > self.x - 1: i = self.x - 1
		if j < 0: j = 0
		elif j > self.y - 1: j = self.y - 1
		
		if type(self.value[i][j]) is str : return 0
		return self.value[i][j]
	
test = ValueIteration(-1,-1,-1, -1)
test.printOut()
test.iteration(10)
#MAX( p1*(rUP + G *V(sUP)) + p2 *(rUP + G * V(sNoChange)) + (p1 + p2 - 1)/2 *(rUP + G *V(sUpLeft)) + (p1 + p2 - 1)/2 *(rUP + G *V(sUpRight)),