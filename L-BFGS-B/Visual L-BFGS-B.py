import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import scipy.optimize as opt

def generate_random_cities_coordinates(num_cities, seed=42):
    np.random.seed(seed)
    cities_coordinates = np.random.rand(num_cities, 2) * 100
    return cities_coordinates

def create_distance_matrix(cities_coordinates):
    num_cities = cities_coordinates.shape[0]
    distance_matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = np.linalg.norm(cities_coordinates[i] - cities_coordinates[j])
            distance_matrix[i, j] = distance_matrix[j, i] = distance

    return distance_matrix

def tsp_optimal_solution(distance_matrix):
    num_cities = distance_matrix.shape[0]
    x0 = np.random.permutation(np.arange(1, num_cities))
    
    def objective_function(x):
        total_distance = 0
        route = np.concatenate(([0], x, [0]))
        for i in range(num_cities):
            total_distance += distance_matrix[int(route[i]), int(route[i+1])]
        return total_distance
    
    bounds = [(1, num_cities - 1)] * (num_cities - 1)
    result = opt.minimize(objective_function, x0, method='L-BFGS-B', bounds=bounds)
    optimal_route = np.concatenate(([0], result.x.astype(int), [0]))
    optimal_distance = objective_function(result.x)
    
    return optimal_distance, optimal_route


def plot_tsp_solution(cities_coordinates, optimal_route):
    fig, ax = plt.subplots()
    optimal_route_coords = np.concatenate([cities_coordinates[optimal_route], cities_coordinates[[optimal_route[0]]]], axis=0)

    line, = ax.plot([], [], 'o-', animated=True)

    def update(frame):
        line.set_data(optimal_route_coords[:frame + 1, 0], optimal_route_coords[:frame + 1, 1])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(optimal_route_coords), blit=True, interval=500, repeat=False)

    ax.set_xlim(np.min(cities_coordinates[:, 0]) - 1, np.max(cities_coordinates[:, 0]) + 1)
    ax.set_ylim(np.min(cities_coordinates[:, 1]) - 1, np.max(cities_coordinates[:, 1]) + 1)
    plt.show()

num_cities = 100
cities_coordinates = generate_random_cities_coordinates(num_cities)
distance_matrix = create_distance_matrix(cities_coordinates)
optimal_distance, optimal_route = tsp_optimal_solution(distance_matrix)
plot_tsp_solution(cities_coordinates, optimal_route)
