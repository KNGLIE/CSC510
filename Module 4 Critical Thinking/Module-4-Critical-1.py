from simpleai.search import SearchProblem, astar


# using SearchProblem and astar from simpleai.search, interactive script using astar for traveling salesman problem

# define the problem
class TSP(SearchProblem):
    def __init__(self, initial, matrix):
        self.matrix = matrix
        super(TSP, self).__init__(initial_state=tuple(initial))

    # This is a function that returns a list of actions
    def actions(self, state):
        # Create an empty list of actions
        actions = []
        # Loop through the matrix
        for i in range(len(self.matrix)):
            # If the index is not in the state
            if i not in state:
                # Add the index to the list of actions
                actions.append(i)
        # Return the list of actions
        return actions

    def result(self, state, action):
        # Create a new state by appending the action to the current state
        new_state = list(state)
        new_state.append(action)
        return tuple(new_state)
        # Check if the length of the state is equal to the number of nodes

    def is_goal(self, state):
        return len(state) == len(self.matrix)
        # Return the cost of the edge between the last node in the state and the action

    def cost(self, state1, action, state2):
        # Return the maximum cost of the edges between the last node in the state and the unvisited nodes
        return self.matrix[state1[-1]][action]

    def heuristic(self, state):
        not_visited = [x for x in range(len(self.matrix)) if x not in state]
        if not_visited:
            return max([self.matrix[state[-1]][x] for x in not_visited])
        else:
            return 0


# define the matrix
matrix = [[0, 2, 9, 10],
          [1, 0, 6, 4],
          [15, 7, 0, 8],
          [6, 3, 12, 0]]

# define the initial state
initial = [0]

# solve the problem
problem = TSP(initial, matrix)
result = astar(problem)

# print the result
print('The optimal path is: ' + str(result.state) + ' with a cost of ' + str(result.cost))
