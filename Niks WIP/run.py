import gridworldtestbed as GTB

print("Time for some GridWorld Wandering")
print("Do you want: ")
q = input("Monte Carlo put 1, SARSA put 2, or Q-Learning put 3\n")
mc = False
sa = False
qLearning = False

if q == "1":
	mc = True
elif q == "2":
	sa = True
elif q == "3":
	qLearning = True
else:
	print("I didn't understand your input, so we will do Monte Carlo")
	mc = True
print("The default settings are: \n\tp1 = 0.8\n\tp2 = 0.1")
p1 = 0.8
p2 = 0.1
choice = input("Do you want to change these defaults? Y/N\n")
if choice == "Y" or choice =="y":
	p1 = double(input("p1 = "))
	p2 = double(input("p2 = "))
choice = input("The defaults for \n\tgamma = 0.9\n\talpha = 0.1\n\tepsilon = 0.1 \ndo you want to change them?\n Y/N\n")
gamma = 0.9
alpha = 0.1
epsilon = 0.1
if choice == "Y" or choice =="y":
	gamma = double(input("gamma = "))
	alpha = double(input("alpha = "))
	epsilon = double(input("epsilon = "))
print("Number of Iterations is set to 1 and episodes equals 200 with maxiumum steps per episode set to 1000")
iterations = 1
episodes = 200
steps = 1000
choice = input("Do you want to change these? Y/N\n")
if choice == "Y" or choice =="y":
	iterations = input("Iterations: ")
	episodes = input("Episodes: ")
	steps = input("Maximum steps: ")
	
test = GTB.testbed(mc,sa,qLearning,p1, p2, epsilon, gamma, alpha)
test.run(iterations, episodes, steps)