# Name, Student Number
# Oluwatomilayo Adegbite, 500569283
# Nikolas Maier, 500461990
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
	#mc = True
	qLearning = True
	#sa = True
	print("I didn't understand your input, so we will do MC: {} , SARSA: {}, Q-L: {}".format(mc,sa,qLearning))
	

p1 = 1
p2 = 0

print("The default settings are: \n\tp1 = {}\n\tp2 = {}".format(p1,p2))

choice = input("Do you want to change these defaults? Y/N\n")
if choice == "Y" or choice =="y":
	p1 = float(input("p1 = "))
	p2 = float(input("p2 = "))

gamma = 0.9
alpha = 0.1
epsilon = 0.1

choice = input("The defaults for \n\tgamma = {}\n\talpha = {}\n\tepsilon = {} \ndo you want to change them?\n Y/N\n".format(gamma,alpha,epsilon))

if choice == "Y" or choice =="y":
	gamma = float(input("gamma = "))
	alpha = float(input("alpha = "))
	epsilon = float(input("epsilon = "))

iterations = 1
episodes = 300
steps = 5000

print("Number of Iterations is set to {} and episodes equals {} with maxiumum steps per episode set to {}".format(iterations,episodes,steps))

choice = input("Do you want to change these? Y/N\n")
if choice == "Y" or choice =="y":
	iterations = int(input("Iterations: "))
	episodes = int(input("Episodes: "))
	steps = int(input("Maximum steps: "))

print("Iterations: {}, Episodes: {}, Steps: {}\nStarting...".format(iterations,episodes,steps))
test = GTB.testbed(mc,sa,qLearning,p1, p2, epsilon, gamma, alpha)
test.run(iterations, episodes, steps)
input("Press Enter key to exit")