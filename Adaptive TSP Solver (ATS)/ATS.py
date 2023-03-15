import random
import numpy as np
import math
from scipy.spatial import distance_matrix
from sklearn.utils import shuffle
from tsp_solver2.greedy import solve_tsp


def haversine_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371  # Earth's radius in km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

def adaptive_tsp_solver(coordinates, num_iterations=1000, population_size=50, mutation_rate=0.1, crossover_rate=0.9, ant_colony_iterations=100, alpha=1, beta=5, rho=0.5, q0=0.9, elitism_factor=5):
    num_locations = len(coordinates)
    dist_matrix = np.array([[haversine_distance(c1, c2) for c2 in coordinates] for c1 in coordinates])

    def tsp_objective_function(route, distance_matrix):
        indices = np.array(route, dtype=int)
        indices = np.append(indices, indices[0])
        total_distance = np.sum(distance_matrix[indices[:-1], indices[1:]])
        return total_distance

    def greedy_initial_solution(distance_matrix):
        return solve_tsp(distance_matrix)

    def two_opt(route, distance_matrix):
        def swap_2opt(route, i, k):
            new_route = route[:i]
            new_route.extend(reversed(route[i:k+1]))
            new_route.extend(route[k+1:])
            return new_route

        best_route = route[:]
        improved = True

        while improved:
            improved = False
            for i in range(1, len(route) - 2):
                for k in range(i + 1, len(route) - 1):
                    new_route = swap_2opt(best_route, i, k)
                    if tsp_objective_function(new_route, distance_matrix) < tsp_objective_function(best_route, distance_matrix):
                        best_route = new_route
                        improved = True

        return best_route

    def three_opt(route, distance_matrix):
        def swap_3opt(route, i, j, k):
            return route[:i+1] + route[j:i:-1] + route[j+1:k+1] + route[k+1:]

        best_route = route[:]
        improved = True

        while improved:
            improved = False
            for i in range(0, len(route) - 3):
                for j in range(i + 1, len(route) - 2):
                    for k in range(j + 1, len(route) - 1):
                        new_route = swap_3opt(best_route, i, j, k)
                        if tsp_objective_function(new_route, distance_matrix) < tsp_objective_function(best_route, distance_matrix):
                            best_route = new_route
                            improved = True

        return best_route

    # Genetic Algorithm functions
    def random_permutation(size):
        return np.random.permutation(size).tolist()

    def crossover(parent1, parent2):
        child = [None] * len(parent1)
        start, end = sorted(random.sample(range(len(parent1)), 2))

        child[start:end+1] = parent1[start:end+1]

        remaining = [x for x in parent2 if x not in child]

        for i in range(len(child)):
           
            if child[i] is None:
                child[i] = remaining.pop(0)

        return child

    def mutate(route):
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]


    def genetic_algorithm(population, distance_matrix, num_iterations, mutation_rate, crossover_rate):
        def population_diversity(population):
            unique_individuals = len(set(tuple(individual) for individual in population))
            return unique_individuals / len(population)

        def adaptive_mutation_rate(base_mutation_rate, population_diversity, diversity_threshold=0.6, factor=1.5):
            if population_diversity < diversity_threshold:
                return base_mutation_rate * factor
            return base_mutation_rate

        for _ in range(num_iterations):
            new_population = []
            diversity = population_diversity(population)
            adaptive_rate = adaptive_mutation_rate(mutation_rate, diversity)

            for _ in range(population_size):
                parent1 = random.choice(population)
                parent2 = random.choice(population)

                if random.random() < crossover_rate:
                    child = crossover(parent1, parent2)
                else:
                    child = random.choice([parent1, parent2]).copy()

                if random.random() < adaptive_rate:
                    mutate(child)

                new_population.append(child)

            population = new_population

        return min(population, key=lambda x: tsp_objective_function(x, distance_matrix))


    # Initial solution
    initial_solution = greedy_initial_solution(distance_matrix)
    refined_solution = two_opt(initial_solution, distance_matrix)
    refined_solution = three_opt(refined_solution, distance_matrix) 

    # Generate initial population
    population = [refined_solution]

    for _ in range(population_size - 1):
        mutated = refined_solution.copy()
        mutate(mutated)
        population.append(mutated)

    # Apply Genetic Algorithm
    final_solution = genetic_algorithm(population, distance_matrix, num_iterations, mutation_rate, crossover_rate)

    return final_solution

# Générer 512 nœuds aléatoires pour l'exemple
num_nodes = 512
coordinates = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_nodes)]

# Appliquer l'algorithme ATS
optimal_route = adaptive_tsp_solver(coordinates, num_iterations=1000, population_size=50, mutation_rate=0.1, crossover_rate=0.9)

print("Optimal route (indices):")
print(optimal_route)

print("Optimal route (coordinates):")
for idx in optimal_route:
    print(coordinates[idx])
