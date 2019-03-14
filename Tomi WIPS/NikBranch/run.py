import grids
import agent

gridWorld = grids.gridWorld(4,4)
gridWorld.fill()
print(str(gridWorld))
newAgent = agent.agent("Agent1", gridWorld)
print(newAgent.position)
newAgent.moveDown()
print("X:{}, Y:{}".format(newAgent.x, newAgent.y))
newAgent.moveDown()
print("X:{}, Y:{}".format(newAgent.x, newAgent.y))
newAgent.moveDown()
print("X:{}, Y:{}".format(newAgent.x, newAgent.y))
newAgent.moveDown()
print("X:{}, Y:{}".format(newAgent.x, newAgent.y))
newAgent.moveDown()
print("X:{}, Y:{}".format(newAgent.x, newAgent.y))