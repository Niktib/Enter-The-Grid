import GridWorld
import gridAgent
import random

debug = True
class testbed:

    def __init__(self, randomSpwan=False):
        self.gridWorld = GridWorld.GridWorld(start={"grid": 3, "x" : 2 , "y" : 2}, goal={"grid": 3, "x" : 1 , "y" : 3})
        if randomSpwan:
            agent = gridAgent.Agent(self.gridWorld,None)
        else:
            agent = gridAgent.Agent(self.gridWorld,None)

        self.gridWorld.pieceItTogether()
        self.gridWorld.insertAgent(agent)


    def run(self, iterations, episodes):
        for iter in range(1, iterations+1):
            self.gridWorld.resetGrid(2,2,3)
            for ep in range(1,episodes+1):
                if self.gridWorld.agent.Done:
                    print("*******************Found Goal******************\nFinal Stats: {}\n***********************************************".format(self.gridWorld.agent.playerStatus())) if debug else False
                    break
                #self.gridWorld.printOut()
                self.gridWorld.agentMove()
                print("Iter: {}, Ep: {}, {}".format(iter, ep, self.gridWorld.agent.playerStatus())) if debug else False #debug

test = testbed()
test.run(3, 10)
