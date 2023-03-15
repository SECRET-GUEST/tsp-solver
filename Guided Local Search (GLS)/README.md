```
 ██████╗    ██╗        ███████╗   
██╔════╝    ██║        ██╔════╝   
██║  ███╗   ██║        ███████╗   
██║   ██║   ██║        ╚════██║   
╚██████╔╝██╗███████╗██╗███████║██╗
 ╚═════╝ ╚═╝╚══════╝╚═╝╚══════╝╚═╝
                                  
```

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


