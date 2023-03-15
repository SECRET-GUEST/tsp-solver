```
 █████╗     ██████╗    ██████╗          ██╗           ██████╗ ███████╗ ██████╗ ███████╗      ██████╗ 
██╔══██╗   ██╔════╝   ██╔═══██╗         ██║           ██╔══██╗██╔════╝██╔════╝ ██╔════╝      ██╔══██╗
███████║   ██║        ██║   ██║   █████╗██║     █████╗██████╔╝█████╗  ██║  ███╗███████╗█████╗██████╔╝
██╔══██║   ██║        ██║   ██║   ╚════╝██║     ╚════╝██╔══██╗██╔══╝  ██║   ██║╚════██║╚════╝██╔══██╗
██║  ██║██╗╚██████╗██╗╚██████╔╝██╗      ███████╗      ██████╔╝██║     ╚██████╔╝███████║      ██████╔╝
╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝      ╚══════╝      ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝      ╚═════╝ 
                                                                                                                                                                                                                                                                                                       
```

# ACO-LBFGS algorithm



The ACO-LBFGS algorithm presented here is a combination of an Ant Colony Optimization (ACO) algorithm and the Limited-memory Broyden–Fletcher–Goldfarb–Shanno (L-BFGS-B) optimization algorithm to solve the Traveling Salesman Problem (TSP). This hybrid approach aims to leverage the global search properties of ACO and the local search capabilities of L-BFGS-B to efficiently find an optimal or near-optimal solution to the TSP.

- Script 1, "Google-VS-L-BFGS-B.py," solves the TSP using Google Maps API for calculating real distances between locations and L-BFGS-B to find the optimal route. It defines a distance matrix using Google Maps API, an objective function that computes the total distance of a route, and a function to solve the TSP using L-BFGS-B.

- Script 2, "L-BFGS-B.py," solves the TSP using random city coordinates and L-BFGS-B. It generates random city coordinates, computes the distance matrix using Euclidean distances, and defines the same objective function and L-BFGS-B solver as in Script 1.

- Script 3, "Visual L-BFGS-B.py," is similar to Script 2, but it includes visualization of the optimal TSP route using Matplotlib.

- Script 4, "Visual-Google-VS-L-BFGS-B.py," is a combination of Script 1 and 3, using Google Maps API to compute distances and visualizing the results with gmaps.


The L-BFGS-B algorithm is an optimization method used for solving nonlinear optimization problems with bound constraints. It is a variant of the Limited-memory Broyden–Fletcher–Goldfarb–Shanno (L-BFGS) algorithm, which itself is a memory-efficient version of the Broyden–Fletcher–Goldfarb–Shanno (BFGS) algorithm. The BFGS algorithm is a popular Quasi-Newton optimization method used for finding local minima of smooth functions.

The L-BFGS-B algorithm is particularly useful when the number of variables in the optimization problem is large, and when some of the variables have constraints on their possible values. It approximates the inverse Hessian matrix using a limited amount of computer memory, which makes it more efficient for large-scale optimization problems.

The algorithm was developed by Ciyou Zhu, Richard Byrd, Jorge Nocedal, and Jose Luis Morales. You can find the original paper describing the L-BFGS-B algorithm here:

https://dl.acm.org/doi/10.1145/279232.279236

For more information and resources on L-BFGS and L-BFGS-B algorithms, you can check out the following links:

https://en.wikipedia.org/wiki/Limited-memory_BFGS

http://users.iems.northwestern.edu/~nocedal/, one of the authors of the L-BFGS-B algorithm

https://docs.scipy.org/doc/scipy/reference/optimize.minimize-lbfgsb.html


## The L-BFGS-B algorithm is employed in solving the TSP as follows:

1. Define the objective function to minimize, which is the total distance of a route:

`f(x) = Σ (distance_matrix[route[i], route[i+1]])`

where `x` is a permutation of the city indices and `distance_matrix[i, j]` represents the distance between cities `i` and `j`.

2. Set the initial solution `x0` as a random permutation of city indices.

3. Define the bounds for the optimization variables, ensuring that the city indices remain within the valid range.

4. Minimize the objective function using the L-BFGS-B optimization algorithm with the defined bounds.

In summary, the ACO-LBFGS algorithm leverages the L-BFGS-B optimization method to solve the TSP efficiently. 
The four scripts provided cover different aspects of the problem, including using real-world data from Google Maps API and visualizing the solutions.

