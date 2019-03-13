import GridWorld
import gridAgent
import random
import mc
import q
import sarsa

debug = False
class testbed:

	#Also all those greek letters
	
	def __init__(self, mcLearning = False, sarsaLearning = False, qLearning = False, randomSpwan=False):
		self.gridWorld = GridWorld.GridWorld({"grid": 3, "x" : 4 , "y" : 0})
		self.gridWorld.pieceItTogether()
		
		self.mcLearning = mcLearning
		self.sarsaLearning = sarsaLearning
		self.qLearning = qLearning
		
		if self.mcLearning: self.policy = mc.monteCarlo()
		if self.sarsaLearning: self.policy = sarsa.sarsaLearning()
		if self.qLearning: self.policy = q.qlearning()
		
		
	def run(self, iterations, episodes):
		totalSuccess = 0
		
		agentArray= [[0,3,3],[0,2,3], [0,1,3], [1,4,3],[2,4,3],[random.randint(0,4), random.randint(0,4), 3],[random.randint(0,4), random.randint(0,4), 3],[random.randint(0,4), random.randint(0,4), 3],[random.randint(0,4), random.randint(0,4), 3]]
		
		for i in range(episodes - len(agentArray) +1): agentArray.append([random.randint(0,4),random.randint(0,4),random.randint(0,len(self.gridWorld.arrayOfGrids)-1)+1])
		
		for iter in range(1, iterations+1):
			
			agent = gridAgent.Agent(2,3,3,self.policy)
			agent.playerStateSetUp(self.gridWorld.understandingState())
			for ep in range(1,episodes+1):
				while True:
					print("Iter: {}, Ep: {}, {}".format(iter, ep, agent.playerStatus()))
					self.gridWorld.printOut(agent.agentState(), True)

					agent.results(self.gridWorld.agentMove(agent.agentState(), agent.move()))
					if self.sarsaLearning or self.qLearning: agent.sarsaUpdate()
					print("Iter: {}, Ep: {}, {}".format(iter, ep, agent.playerStatus())) if debug else False#debug
					#Check if goal state has been reached?
					if self.gridWorld.finished: totalSuccess += 1
					if self.gridWorld.finished or len(agent.stateActionArray) > 1000:
						#Reset goal state
						self.gridWorld.finished = False
						break
				#At end of episode, update policy and grab it from agent to give to new agent
				if self.mcLearning: agent.mcUpdate()
				
				self.policy = agent.policyRetrieval()
				agent = gridAgent.Agent(0,3,3,self.policy)
				#agent = gridAgent.Agent(agentArray[ep][0],agentArray[ep][1],agentArray[ep][2] ,self.policy)
		print("The total # of successful runs: {}".format(totalSuccess))
		self.policy.printOut()
test = testbed(False,False,True)
test.run(1, 200)
