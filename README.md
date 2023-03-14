`P=NP` ? merely a question of time
```
___ ____ ___     ____ _    ____ ____ ____ _ ___ _  _ _  _ 
 |  [__  |__]    |__| |    | __ |  | |__/ |  |  |__| |\/| 
 |  ___] |       |  | |___ |__] |__| |  \ |  |  |  | |  | 
                                                          
```                            
                            
# Introduction                            

Just playing with GPT-4 with solving random crypto algorithms such as **P = NP** or other cryptographic problems to rule the wolrdlrd in the sh4d0w. Don't thx me it's for the buzz lol^^<3

# The Adaptive TSP Solver (ATS)

The Adaptive TSP Solver (ATS) is a novel hybrid approach designed to efficiently solve the Traveling Salesman Problem by leveraging the strengths of various techniques. ATS combines elements from exact methods, heuristics, and metaheuristics to strike a balance between solution quality and computational time. It employs a hierarchical structure that initially uses a fast, greedy heuristic (e.g., nearest neighbor or minimum spanning tree) to generate an initial solution. This solution is then refined by applying local search methods, such as 2-opt or 3-opt, to further improve its quality.

To address the challenge of finding a globally optimal solution, ATS integrates population-based search algorithms like Genetic Algorithms or Ant Colony Optimization. These metaheuristics help the algorithm escape local optima and explore the solution space more effectively. Additionally, ATS incorporates adaptive mechanisms to dynamically adjust its parameters and search strategies based on the problem instance and the progress of the search.

Overall, the Adaptive TSP Solver is designed to provide good-quality solutions for various TSP instances within a reasonable time frame, without guaranteeing optimality. It is well-suited for large-scale problems where a trade-off between solution quality and computational time is desired.

This method has been created by GPT-4 under my direction.

# Guided Local Search (GLS)

Guided Local Search (GLS) is a metaheuristic algorithm for combinatorial optimization problems, such as the Traveling Salesman Problem (TSP). The algorithm uses local search methods and adds a penalty term to guide the search process towards better solutions. In the case of the TSP, the GLS aims to find the shortest route that visits all the cities exactly once and returns to the starting city.

The code you provided follows these steps:

Calculate the Haversine distance between all pairs of coordinates to create a distance matrix.
Use the nearest neighbor heuristic to generate an initial solution (route) based on the distance matrix.
Apply the 2-opt optimization to the initial solution to improve the route.
Perform local search using a tabu list (a list of prohibited moves) to avoid cycling and revisiting previously visited solutions.
Add penalties to the distance matrix based on the current route to guide the search towards better solutions.
Repeat the local search and penalty updates for a fixed number of iterations (max_iterations).

#  "Ant Colony Optimization" (ACO)

The scripts called "Ant Colony Optimization" (ACO) is an optimization method inspired by the behavior of ants when searching for a path between their colony and a food source. The algorithm uses pheromones to simulate the communication and exploration behavior of ants in nature.

There are 2 script one with a graphical representation the other with only the answer in a terminal.

# L-BFGS-B

There are 4 scripts, 2 using the google API to solve the TSP on google map, one with visual and the other faster with the answer in the terminal.

The L-BFGS-B algorithm is an optimization method used for solving nonlinear optimization problems with bound constraints. It is a variant of the Limited-memory Broyden–Fletcher–Goldfarb–Shanno (L-BFGS) algorithm, which itself is a memory-efficient version of the Broyden–Fletcher–Goldfarb–Shanno (BFGS) algorithm. The BFGS algorithm is a popular Quasi-Newton optimization method used for finding local minima of smooth functions.

The L-BFGS-B algorithm is particularly useful when the number of variables in the optimization problem is large, and when some of the variables have constraints on their possible values. It approximates the inverse Hessian matrix using a limited amount of computer memory, which makes it more efficient for large-scale optimization problems.

The algorithm was developed by Ciyou Zhu, Richard Byrd, Jorge Nocedal, and Jose Luis Morales. You can find the original paper describing the L-BFGS-B algorithm here:

https://dl.acm.org/doi/10.1145/279232.279236

For more information and resources on L-BFGS and L-BFGS-B algorithms, you can check out the following links:

https://en.wikipedia.org/wiki/Limited-memory_BFGS

http://users.iems.northwestern.edu/~nocedal/, one of the authors of the L-BFGS-B algorithm

https://docs.scipy.org/doc/scipy/reference/optimize.minimize-lbfgsb.html
