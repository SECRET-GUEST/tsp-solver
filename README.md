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




# Guided Local Search (GLS)

This algorithm presents a Guided Local Search (GLS) approach to solve the Traveling Salesman Problem (TSP) using the Haversine distance formula, nearest neighbor heuristic, and 2-opt optimization.

The Haversine distance formula is used to calculate the great-circle distance between two points on a sphere, given their latitude and longitude coordinates:


`d = 2 * R * atan2(sqrt(a), sqrt(1 - a))`

Where d is the distance between two points, R is the Earth's radius (approximately 6,371 km), and a is calculated as follows:

`a = sin²(dlat/2) + cos(lat1) * cos(lat2) * sin²(dlon/2)`
dlat and dlon are the differences in latitudes and longitudes, respectively, between the two points.

The algorithm initializes the solution using the nearest neighbor heuristic, followed by a 2-opt optimization to refine the solution. The guided local search is then performed using an augmented distance matrix with penalty values, and a tabu list to prevent cycling through previously visited solutions.

### The GLS algorithm performs the following steps:

1. Create a distance matrix using the Haversine distance formula.

2. Generate an initial solution using the nearest neighbor heuristic.

3. Apply the 2-opt optimization to the initial solution.

4. Perform local search using the augmented distance matrix and tabu list.

5. Update the penalties and tabu list based on the obtained solution.

6. Repeat steps 4-5 for the specified number of iterations.

The output is the optimal route found by the algorithm, represented as a list of indices corresponding to the input coordinates.





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
