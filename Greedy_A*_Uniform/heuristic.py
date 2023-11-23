#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# Comments:
# The entirety of this code was created via a conjunction of review/relearning of how a heuristic function works in
# tandem with A* search, how it incorporates euclidean distance, and a conversation with Nick Mount and
# Andrew Mouillesseaux to help me determine the potential way of implementing heuristic and the overall concept
# behind it. Essentially, based on lecture I found that the value that needs to be returned is the time cost.
# Time cost, in general, was to be calculated by dividing Euclidean distance between our location and and problem goal,
# by the maximum mpg. Thanks to my conversation with Andrew I learnt that we wanted the largest mpg to minimize the
# heuristic function and thus make it more "admissable". The euclidean distance portion was easy to understand and
# implement. It was calculating the maximum mpg that proved to be difficult. All I knew, thanks to a conversation with
# Nick, was that mpg was calculated by dividing distance by gas amount and that I needed to loop through the locations
# and connections to each location in order to find the maximum mpg. However, it wasn't until I looked back at
# PA1Spec.pdf that I found out that the road cost was equivalent to the gas amount, which I took to be the
# action_cost function in route.py. From here, constructing the rest of the code and comparing my self.max_mpg to the
# current mpg, proved to be work.
#
#
# Citations:
# PA1Spec.pdf -> Greedy Search pseudocode that was provided
# PA1Spec.pdf -> A* Search pseudocode that was provided
# PA1Spec.pdf -> Uniform Cost Search pseudocode that was provided
# PASpec.pdf -> action_cost = road cost = gas amount
# https://www.geeksforgeeks.org/greedy-best-first-search-algorithm/ -> Review on Greedy Search
# https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/ -> Review on Uniform Cost Search
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ -> Review on Dijkstra (for ucost)
# https://blog.finxter.com/python-__delitem__-magic-method/ -> Utilizing front_init.__delitem__(child)
# https://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html -> Understanding of Heuristic + A* search
# https://brilliant.org/wiki/a-star-search/#heuristics -> Understanding + Overestimation of Heuristic
# Conversation with Nick Mount and Andrew Mouillesseaux on Heuristic Function Concept + how to go about implementing it
#
#
# Acknowledgements:
# Nick Mount -> Helped understand concept behind Heuristic Function
# Andrew Mouillesseaux -> Helped understand concept behind Heuristic Function + how to go about implementing it
#
#
# Esha Sarfraz - September 29, 2023
#



import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem

        # PLACE ANY INITIALIZATION CODE HERE

        # Set our map as our problem map
        self.map = problem.map

        # Set our goal as our problem goal
        self.goal = problem.goal

        # Initialize our max mpg to be 0
        self.max_mpg = 0.0

        # For each location in the problem map
        for location in self.map.locations():

            # For each connection at each location + roads at that location
            for connection in self.map.connection_dict:

                # Get the road cost or amount of gas from the location to the connection of that location
                gas_amount = problem.action_cost(location, connection)

                # Set our current distance equal to the euclidean distance between that location and its connection
                current_distance = problem.map.euclidean_distance(location, connection)

                # If our road cost/gas amount is not Null
                if gas_amount is not None:

                    # Calculate our current mpg to the current distance over the road cost/gas amount
                    current_mpg = current_distance / gas_amount

                    # If our current mpg is greater than the max mpg we want
                    if current_mpg > self.max_mpg:

                        # We set our max mpg as our current mpg
                        self.max_mpg = current_mpg


    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE

            # Find our euclidean distance between our location and our problem goal
            euclidean_distance = self.map.euclidean_distance(loc, self.goal)

            # Set our time cost value equal to the euclidean distance divided by our maximum mpg
            value = euclidean_distance / self.max_mpg

            # Return our time cost value
            return value
