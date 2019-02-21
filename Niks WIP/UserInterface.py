import pia as PIA
import via as VIA

print("Let's run some Dynamic Programming \n")
print("First pick which kind of Iteration you want: \n")

print("Policy Iteration = 1 \nValue Iteration = 2")
typeIteration = input("Which type: ")

print("The default values are as follows: \np1 = 0.8\np2 = 0.1\nAll Rewards = -1\nGrid is 4x4\n")
p1 = 0.8
p2 = 0.1
rUp = -1
rDown = -1
rLeft = -1
rRight = -1
width = 4
length = 4

option = input("Do you want to change anything? (Y/N): ")
if option == "Y" or option == "y":
	p1 = float(input("p1: "))
	p2 = float(input("p2: "))
	rUp = float(input("Up Reward: "))
	rDown = float(input("Down Reward: "))
	rLeft = float(input("Left Reward: "))
	rRight = float(input("Right Reward: "))
	width = int(input("Width: "))
	length = int(input("Length: "))

printingGrid = False
choosing = input("One last choice, do you want the values printed out in a grid formation? (Y/N): ")
if choosing == "Y" or choosing == "y": 	printingGrid = True

if typeIteration == 1:
	test = PIA.PolicyIteration(p1,p2,rUp,rDown,rLeft,rRight,width,length)
	if printingGrid: test.printOut()
	test.policyIterating(1000, printingGrid)
else:
	test = VIA.ValueIteration(p1,p2,rUp,rDown,rLeft,rRight,width,length)
	if printingGrid: test.printOut()
	test.iteration(10000, printingGrid)

'''
print("Policy Iteration:\n")
test = PIA.PolicyIteration(0.8,0.1,-1,-1,-1,-1,4,4)
test.policyIterating(1000)

print("Value Iteration:\n")
test = VIA.ValueIteration(0.8,0.1,-1,-1,-1,-1,4,4)
test.iteration(10000)
'''