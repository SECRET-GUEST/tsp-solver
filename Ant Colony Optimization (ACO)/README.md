```
 █████╗     ██████╗    ██████╗    
██╔══██╗   ██╔════╝   ██╔═══██╗   
███████║   ██║        ██║   ██║   
██╔══██║   ██║        ██║   ██║   
██║  ██║██╗╚██████╗██╗╚██████╔╝██╗
╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝
                                  
```

# Ant Colony Optimization (ACO)

The given algorithms aim to solve the Traveling Salesman Problem (TSP) using Ant Colony Optimization (ACO). 

The TSP objective is to find the shortest possible route for a salesman visiting a set of cities, only visiting each city once, and returning to the starting city.

The ACO algorithm simulates the foraging behavior of ants in finding an optimal path. 

It consists of the following components:

1. Euclidean distance calculation: `euclidean_distance(p1, p2)`, which computes the straight-line distance between two points using the formula `√((x2 - x1)^2 + (y2 - y1)^2)`.

2. Distance matrix creation: `create_distance_matrix(points)` builds a symmetric matrix with the distances between all pairs of cities.

3. Pheromone initialization: initialize_pheromones(n) sets an initial equal amount of pheromone for each city pair.

4. Next city selection: `select_next_city(current_city, unvisited_cities, distance_matrix, pheromones, alpha, beta)` calculates the probabilities of visiting each remaining city based on pheromone levels and distances. 
The probability is proportional to `τ^α * (1/d)^β`, where `τ` is the pheromone level, `d` is the distance, and `α` and `β` are parameters controlling the influence of pheromones and distances.

5. Ant Colony Optimization: `ant_colony_optimization(points, n_ants, n_iterations, alpha, beta, evaporation_rate)` iteratively runs the algorithm with a given number of ants and iterations. In each iteration, ants construct their tours, update pheromones, and evaporate a fraction of pheromones. The algorithm keeps track of the best tour found.

The second version of the algorithm includes a graphical display of the best tour found during each iteration. 
It incorporates an additional function `display_path(points, tour, iteration, length)` that visualizes the cities, their connections, and the best tour length at a given iteration. This version provides a more interactive way to observe the optimization process.
