import GridWorld
import gridAgent
import random
import mc
import q
import sarsa

debug = True
class testbed:

	def __init__(self, randomSpwan=False):
		self.gridWorld = GridWorld.GridWorld({"grid": 2, "x" : 2 , "y" : 2})
		self.gridWorld.pieceItTogether()
		self.policy = mc.monteCarlo()

	def run(self, iterations, episodes):
		for iter in range(1, iterations+1):
			agent = gridAgent.Agent(2,3,2,self.policy)
			agent.playerStateSetUp(self.gridWorld.understandingState())
			for ep in range(1,episodes+1):
				while True:
					self.gridWorld.printOut(agent.agentState())
					agent.results(self.gridWorld.agentMove(agent.agentState(), agent.move()))
					print("Iter: {}, Ep: {}, {}".format(iter, ep, agent.playerStatus())) if debug else False #debug
					#Check if goal state has been reached?
					if self.gridWorld.finished or len(agent.stateActionArray) > 1000:
						#Reset goal state
						self.gridWorld.finished = False
						break
				#At end of episode, update policy and grab it from agent to give to new agent
				self.policy = agent.policyDetails()
				agent = gridAgent.Agent(random.randint(0,4),random.randint(0,4),random.randint(0,len(self.gridWorld.arrayOfGrids)),self.policy)

test = testbed()
test.run(1, 10)
