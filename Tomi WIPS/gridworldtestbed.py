import GridWorld

class testbed:

    def __init__(self):
        self.gridWorld = GridWorld.GridWorld()
    
    def run(self):
        self.gridWorld.pieceItTogether()

test = testbed()
test.run()