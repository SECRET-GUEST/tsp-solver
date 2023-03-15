`P=NP` ? merely a question of time
```
___ ____ ___     ____ _    ____ ____ ____ _ ___ _  _ _  _ 
 |  [__  |__]    |__| |    | __ |  | |__/ |  |  |__| |\/| 
 |  ___] |       |  | |___ |__] |__| |  \ |  |  |  | |  | 
                                                          
```                            
                            
# Introduction                            

In this study, we explore various optimization techniques to tackle the Traveling Salesman Problem (TSP). We investigate the performance of different algorithms, including the Adaptive TSP Solver (ATS), Ant Colony Optimization (ACO), Limited-memory Broyden-Fletcher-Goldfarb-Shanno (L-BFGS-B), and Guided Local Search (GLS). By comparing their effectiveness and computational efficiency, we aim to identify the most suitable approach for solving TSP instances.

# The Adaptive TSP Solver (ATS)

Here there are 2 methods ;

* The Adaptative TSP Solver (ATS)
* Refined Adaptive TSP Solver (RATS)

These methods has been created by GPT-4 under my direction.

## The Adaptative TSP Solver (ATS)

The Adaptative TSP Solver (ATS) is a novel algorithm designed to solve the Traveling Salesman Problem (TSP). The TSP is an NP-hard optimization problem, where a salesman needs to visit a set of cities while minimizing the total travel distance and returning to the starting city. The ATS combines various heuristic methods, including a greedy initial solution, local search optimization techniques such as 2-opt and 3-opt, and a genetic algorithm to explore the solution space efficiently.

The algorithm calculates a distance matrix using the Haversine distance formula, which accounts for the Earth's curvature when dealing with geographical coordinates. The Haversine distance between two points (lat1, lon1) and (lat2, lon2) is calculated as:

`d = 2 * R * arcsin(sqrt(a))`

where R is the Earth's radius (approximately 6,371 km), and

`a = sin²(dlat/2) + cos(lat1) * cos(lat2) * sin²(dlon/2)`

with dlat = lat2 - lat1 and dlon = lon2 - lon1.

The ATS algorithm consists of the following steps:

1.Generate a greedy initial solution using a nearest-neighbor algorithm provided by the tsp_solver2.greedy package. This heuristic aims to find a short route by sequentially visiting the nearest unvisited city.

2.Refine the initial solution using 2-opt and 3-opt local search optimization techniques. These methods iteratively swap city pairs (2-opt) or reverse city subsequences (3-opt) to reduce the total distance.

3.Initialize a population of routes by creating slightly mutated copies of the refined initial solution. The mutation operation consists of swapping two random cities in the route.

4. Apply a genetic algorithm to the population, which consists of the following steps:

   - Compute the population diversity, defined as the ratio of unique individuals to the total population size.

   - Adapt the mutation rate based on the population diversity to maintain a balance between exploration and exploitation. If the diversity is below a threshold, increase the mutation rate by a factor.

   - Perform crossover and mutation operations to generate a new population. The crossover operation combines two parent routes by selecting a random subsequence from one parent and filling the remaining positions with cities from the other parent in their original order.

   - Repeat steps a-c for a predefined number of iterations.

5. Return the best route found by the genetic algorithm as the final solution.

The ATS algorithm is designed to adapt to the problem instance, balancing exploration and exploitation through an adaptive mutation rate in the genetic algorithm. This adaptability allows the algorithm to efficiently find high-quality solutions for a wide range of TSP instances.





## Refined Adaptive TSP Solver (RATS)

Introducing the "Refined Adaptive TSP Solver" (RATS), a variant of the original Adaptive TSP Solver (ATS) algorithm designed to solve the Traveling Salesman Problem (TSP). The RATS algorithm combines various heuristic methods, including a greedy initial solution, local search optimization techniques such as 2-opt, and a genetic algorithm to explore the solution space efficiently.

The algorithm calculates a distance matrix using the Haversine distance formula, which accounts for the Earth's curvature when dealing with geographical coordinates. The Haversine distance between two points (lat1, lon1) and (lat2, lon2) is calculated as:

`d = 2 * R * arcsin(sqrt(a))`

where R is the Earth's radius (approximately 6,371 km), and

`a = sin²(dlat/2) + cos(lat1) * cos(lat2) * sin²(dlon/2)`

with dlat = lat2 - lat1 and dlon = lon2 - lon1.

The RATS algorithm consists of the following steps:

1. Generate a greedy initial solution using a nearest-neighbor algorithm provided by the tsp_solver2.greedy package. This heuristic aims to find a short route by sequentially visiting the nearest unvisited city.

2. Refine the initial solution using the 2-opt local search optimization technique. This method iteratively swaps city pairs to reduce the total distance.

3. Initialize a population of routes by creating slightly mutated copies of the refined initial solution. The mutation operation consists of swapping two random cities in the route.

4. Apply a genetic algorithm to the population, which consists of the following steps:

   - Perform crossover and mutation operations to generate a new population. The crossover operation combines two parent routes by selecting a random subsequence from one parent and filling the remaining positions with cities from the other parent in their original order.

   - Repeat step a for a predefined number of iterations.

5.Return the best route found by the genetic algorithm as the final solution.

The RATS algorithm is a streamlined version of the ATS algorithm, omitting the 3-opt local search optimization and the adaptive mutation rate adjustment. This simplification can lead to faster computation times while still providing high-quality solutions for a wide range of TSP instances.











# Guided Local Search (GLS)

Guided Local Search (GLS) is a metaheuristic algorithm for combinatorial optimization problems, such as the Traveling Salesman Problem (TSP). 

The algorithm uses local search methods and adds a penalty term to guide the search process towards better solutions.

In the case of the TSP, the GLS aims to find the shortest route that visits all the cities exactly once and returns to the starting city.


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
