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

This algorithm solves the Traveling Salesman Problem using Guided Local Search (GLS). It employs the Haversine distance, Nearest Neighbor heuristic, and 2-opt optimization to find a near-optimal solution iteratively. The output is an optimal route given as indices and coordinates.


#  "Ant Colony Optimization" (ACO)

The scripts called "Ant Colony Optimization" (ACO) is an optimization method inspired by the behavior of ants when searching for a path between their colony and a food source. The algorithm uses pheromones to simulate the communication and exploration behavior of ants in nature.

There are 2 script one with a graphical representation the other with only the answer in a terminal.


The Ant Colony Optimization (ACO) algorithm is a metaheuristic inspired by the foraging behavior of ants in nature. It is primarily used to solve combinatorial optimization problems, such as the Traveling Salesman Problem (TSP). In ACO, artificial ants iteratively construct solutions by stochastically choosing the next element based on pheromone levels and heuristic information. The pheromone levels are updated by ants to reflect the quality of the solutions found, and they evaporate over time to avoid convergence to a suboptimal solution. The algorithm balances exploration and exploitation to find an optimal or near-optimal solution.



# L-BFGS-B

There are 4 scripts: 2 of them utilize the Google Maps API to solve the TSP, one providing a visual representation and the other offering a quicker solution displayed in the terminal.

1. "Google-VS-L-BFGS-B.py": Compares Google Maps API solution and L-BFGS-B optimization for solving TSP with given addresses, reporting time and route differences.

2. "LBFGSB_algorithm.py": Implements L-BFGS-B optimization for TSP, including distance matrix calculation and visualization of results.

3. "TSP_generator.py": Creates random TSP instances, including customizable number of points, distance range, and output format.

4. "TSP_solver_comparison.py": Evaluates performance of multiple TSP algorithms, comparing L-BFGS-B, genetic algorithm, and Google Maps API, with analysis on time and quality.

