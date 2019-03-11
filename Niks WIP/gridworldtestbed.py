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
        if randomSpwan:
            agent = gridAgent.Agent(random.randint(1,4),random.randint(1,4),random.randint(0,len(self.gridWorld.arrayOfGrids)),mc.monteCarlo())
        else:
            agent = gridAgent.Agent(2,2,3,None)

        self.gridWorld.pieceItTogether()
        self.gridWorld.insertAgent(agent)


    def run(self, iterations, episodes):
        for iter in range(1, iterations+1):
            for ep in range(1,episodes+1):
                self.gridWorld.printOut()
                self.gridWorld.agentMove()
                print("Iter: {}, Ep: {}, {}".format(iter, ep, self.gridWorld.agent.playerStatus())) if debug else False #debug

test = testbed()
test.run(1, 10000)
