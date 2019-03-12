import GridWorld
import gridAgent
import random

debug = True
class testbed:

    def __init__(self, randomSpwan=False):
        start={"grid": 3, "x" : 2 , "y" : 2}
        goal={"grid": 3, "x" : 4 , "y" : 0}
        self.gridWorld = GridWorld.GridWorld(start=start,goal=goal)
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
                    print("*******************Found Goal******************\nFinal Stats:\n{}\n{}\n***********************************************".format(self.gridWorld.agent.playerStatus(),self.gridWorld.agent.policy.printPolicyValue())) if debug else False
                    break
                self.gridWorld.printOut()
                self.gridWorld.agentMove()
                print("Iter: {}, Ep: {}, {}".format(iter, ep, self.gridWorld.agent.playerStatus())) if debug else False #debug
            self.gridWorld.agent.policy.updateStates(self.gridWorld.agent.stateActionArray)
            self.gridWorld.agent.resetAgent(self.gridWorld.startPoint['x'],self.gridWorld.startPoint['y'],self.gridWorld.startPoint['grid'])

test = testbed()
test.run(3, 100)
