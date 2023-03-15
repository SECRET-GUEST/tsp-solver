import random
import numpy as np
from itertools import permutations
from functools import lru_cache
import math

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

def guided_local_search(coordinates, max_iterations=1000, tabu_tenure=10):

    def create_distance_matrix(coordinates):
        num_locations = len(coordinates)
        distance_matrix = np.zeros((num_locations, num_locations))

        for i in range(num_locations):
            for j in range(num_locations):
                distance_matrix[i, j] = haversine_distance(coordinates[i], coordinates[j])

        return distance_matrix

    def nearest_neighbor_heuristic(distance_matrix):
        num_locations = len(distance_matrix)
        unvisited = list(range(1, num_locations))
        route = [0]

        while unvisited:
            last = route[-1]
            nearest_neighbor = min(unvisited, key=lambda x: distance_matrix[last, x])
            route.append(nearest_neighbor)
            unvisited.remove(nearest_neighbor)

        route.append(0)
        return route

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

    def tsp_objective_function(route, distance_matrix):
        indices = np.array(route, dtype=int)
        indices = np.append(indices, indices[0])
        total_distance = np.sum(distance_matrix[indices[:-1], indices[1:]])
        return total_distance


    def local_search(solution, distance_matrix, tabu_list):
        best_delta = float('inf')
        best_move = None

        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if j - i == 1: continue

                delta = (distance_matrix[solution[i - 1], solution[j]] +
                         distance_matrix[solution[i], solution[j + 1]]) - \
                        (distance_matrix[solution[i - 1], solution[i]] +
                         distance_matrix[solution[j], solution[j + 1]])

                if delta < best_delta and (i, j) not in tabu_list:
                    best_delta = delta
                    best_move = (i, j)

        if best_move:
            i, j = best_move
            solution[i:j+1] = reversed(solution[i:j+1])

        return solution, best_delta

    def augment_distance_matrix(distance_matrix, solution, penalties):
        augmented = distance_matrix.copy()
        for i in range(len(solution) - 1):
            augmented[solution[i], solution[i + 1]] += penalties[solution[i], solution[i + 1]]
        return augmented

    distance_matrix = create_distance_matrix(coordinates)
    penalties = np.zeros(distance_matrix.shape, dtype=int)

    initial_solution = nearest_neighbor_heuristic(distance_matrix)
    current_solution = two_opt(initial_solution, distance_matrix)
    current_cost = tsp_objective_function(current_solution, distance_matrix)

    best_solution = current_solution.copy()
    best_cost = current_cost

    tabu_list = []

    for _ in range(max_iterations):
        augmented_distance_matrix = augment_distance_matrix(distance_matrix, current_solution, penalties)
        current_solution, delta = local_search(current_solution, augmented_distance_matrix, tabu_list)

        if delta < 0:
            current_cost += delta
            if current_cost < best_cost:
                best_cost = current_cost
                best_solution = current_solution.copy()

        else:
            i, j = random.randint(1, len(current_solution) - 3), random.randint(2, len(current_solution) - 2)
            penalties[current_solution[i], current_solution[j]] += 1
            penalties[current_solution[j], current_solution[i]] += 1

            tabu_list.append((i, j))
            if len(tabu_list) > tabu_tenure:
                tabu_list.pop(0)

    return best_solution


# Générer 512 nœuds aléatoires pour l'exemple
num_nodes = 512
coordinates = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_nodes)]

# Appliquer la recherche locale guidée (GLS) avec l'heuristique du plus proche voisin et l'optimisation 2-opt
optimal_route = guided_local_search(coordinates, max_iterations=1000, tabu_tenure=10)

print("Optimal route (indices):")
print(optimal_route)

print("Optimal route (coordinates):")
for idx in optimal_route:
    print(coordinates[idx])