
```
 █████╗    ████████╗   ███████╗   
██╔══██╗   ╚══██╔══╝   ██╔════╝   
███████║      ██║      ███████╗   
██╔══██║      ██║      ╚════██║   
██║  ██║██╗   ██║   ██╗███████║██╗
╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝╚══════╝╚═╝
                                  
                               
```

# The Adaptative TSP Solver (ATS)

The Adaptative TSP Solver (ATS) is a novel algorithm designed to solve the Traveling Salesman Problem (TSP). The TSP is an NP-hard optimization problem, where a salesman needs to visit a set of cities while minimizing the total travel distance and returning to the starting city. The ATS combines various heuristic methods, including a greedy initial solution, local search optimization techniques such as 2-opt and 3-opt, and a genetic algorithm to explore the solution space efficiently.

The algorithm calculates a distance matrix using the Haversine distance formula, which accounts for the Earth's curvature when dealing with geographical coordinates. The Haversine distance between two points (lat1, lon1) and (lat2, lon2) is calculated as:

`d = 2 * R * arcsin(sqrt(a))`

where R is the Earth's radius (approximately 6,371 km), and

`a = sin²(dlat/2) + cos(lat1) * cos(lat2) * sin²(dlon/2)`

with dlat = lat2 - lat1 and dlon = lon2 - lon1.

## The ATS algorithm consists of the following steps:

1.Generate a greedy initial solution using a nearest-neighbor algorithm provided by the tsp_solver2.greedy package. This heuristic aims to find a short route by sequentially visiting the nearest unvisited city.

2.Refine the initial solution using 2-opt and 3-opt local search optimization techniques. These methods iteratively swap city pairs (2-opt) or reverse city subsequences (3-opt) to reduce the total distance.

3.Initialize a population of routes by creating slightly mutated copies of the refined initial solution. The mutation operation consists of swapping two random cities in the route.

4. Apply a genetic algorithm to the population, which consists of the following steps:

   - a. Compute the population diversity, defined as the ratio of unique individuals to the total population size.

   - Adapt the mutation rate based on the population diversity to maintain a balance between exploration and exploitation. If the diversity is below a threshold, increase the mutation rate by a factor.

   - b. Perform crossover and mutation operations to generate a new population. The crossover operation combines two parent routes by selecting a random subsequence from one parent and filling the remaining positions with cities from the other parent in their original order.

   - c. Repeat steps a-c for a predefined number of iterations.

5. Return the best route found by the genetic algorithm as the final solution.

The ATS algorithm is designed to adapt to the problem instance, balancing exploration and exploitation through an adaptive mutation rate in the genetic algorithm. This adaptability allows the algorithm to efficiently find high-quality solutions for a wide range of TSP instances.





# Refined Adaptive TSP Solver (RATS)

Introducing the "Refined Adaptive TSP Solver" (RATS), a variant of the original Adaptive TSP Solver (ATS) algorithm designed to solve the Traveling Salesman Problem (TSP). The RATS algorithm combines various heuristic methods, including a greedy initial solution, local search optimization techniques such as 2-opt, and a genetic algorithm to explore the solution space efficiently.

The algorithm calculates a distance matrix using the Haversine distance formula, which accounts for the Earth's curvature when dealing with geographical coordinates. The Haversine distance between two points (lat1, lon1) and (lat2, lon2) is calculated as:

`d = 2 * R * arcsin(sqrt(a))`

where R is the Earth's radius (approximately 6,371 km), and

`a = sin²(dlat/2) + cos(lat1) * cos(lat2) * sin²(dlon/2)`

with dlat = lat2 - lat1 and dlon = lon2 - lon1.

## The RATS algorithm consists of the following steps:

1. Generate a greedy initial solution using a nearest-neighbor algorithm provided by the tsp_solver2.greedy package. This heuristic aims to find a short route by sequentially visiting the nearest unvisited city.

2. Refine the initial solution using the 2-opt local search optimization technique. This method iteratively swaps city pairs to reduce the total distance.

3. Initialize a population of routes by creating slightly mutated copies of the refined initial solution. The mutation operation consists of swapping two random cities in the route.

4. Apply a genetic algorithm to the population, which consists of the following steps:

   - a. Perform crossover and mutation operations to generate a new population. The crossover operation combines two parent routes by selecting a random subsequence from one parent and filling the remaining positions with cities from the other parent in their original order.

   - b. Repeat step a for a predefined number of iterations.

5.Return the best route found by the genetic algorithm as the final solution.

The RATS algorithm is a streamlined version of the ATS algorithm, omitting the 3-opt local search optimization and the adaptive mutation rate adjustment. This simplification can lead to faster computation times while still providing high-quality solutions for a wide range of TSP instances.

