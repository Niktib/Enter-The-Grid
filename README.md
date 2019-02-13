# Enter-The-Grid
	Consider generalized 4x4 Gridworld similar to example 4.1
	Four stochastic actions in each state, 
		A = {u, d, l, r}
	Probabilities:
		p1 probability that agent follows through with an action.
		p2 probability that it takes no action.
		(1-p1-p2)/2 probability agent moves to one of the two states adjacent to the move.
		Actions that move off grid have a p1+p2 probability of no movement, with (1-p1-p2)/2 probability of adjacent state movement.
	Reward:
		r(a) 
	Discount factor:
		0.95
	Accuracy:
		0.001
	Start with equiprobable randompolicy and V(s) = 0 for all states.
	
	Test both algorithms considered in example 4.1 in the text.
	
	Ensure that other numerical data can be used for the 4x4 grid.
	
	Input:
		p1, p2, rUP, rDOWN, rLEFT, rRIGHT
	
	Output: 
		# of iteration
		Computation time (for each iteration)
		Optimal Policy
		
	Report:
		Brief comparison of both algorithms.
