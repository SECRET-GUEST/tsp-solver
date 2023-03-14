import numpy as np
import random
import sys
import matplotlib.pyplot as plt
from time import sleep

# ... (les autres fonctions restent les mêmes)
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(points):
    n = len(points)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            distance_matrix[i][j] = distance_matrix[j][i] = euclidean_distance(points[i], points[j])
    return distance_matrix

def initialize_pheromones(n):
    return np.ones((n, n))

def select_next_city(current_city, unvisited_cities, distance_matrix, pheromones, alpha, beta):
    probabilities = []
    unvisited_cities_list = list(unvisited_cities)
    for city in unvisited_cities_list:
        probability = (pheromones[current_city][city]**alpha) * ((1/distance_matrix[current_city][city])**beta)
        probabilities.append(probability)
    probabilities = np.array(probabilities) / sum(probabilities)
    return np.random.choice(unvisited_cities_list, p=probabilities)

def ant_colony_optimization(points, n_ants=100, n_iterations=100, alpha=1, beta=5, evaporation_rate=0.5, display_progress=True):
    n = len(points)
    distance_matrix = create_distance_matrix(points)
    pheromones = initialize_pheromones(n)

    best_tour = None
    best_length = sys.float_info.max

    for iteration in range(n_iterations):
        all_tours = []
        all_lengths = []

        for ant in range(n_ants):
            start_city = random.randint(0, n-1)
            unvisited_cities = set(range(n)) - {start_city}
            current_city = start_city
            tour = [start_city]

            while unvisited_cities:
                next_city = select_next_city(current_city, unvisited_cities, distance_matrix, pheromones, alpha, beta)
                tour.append(next_city)
                unvisited_cities.remove(next_city)
                current_city = next_city

            tour_length = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(n-1)) + distance_matrix[tour[-1]][tour[0]]
            all_tours.append(tour)
            all_lengths.append(tour_length)

            if tour_length < best_length:
                best_tour = tour
                best_length = tour_length
                if display_progress:
                    display_path(points, best_tour, iteration, best_length)

        pheromones *= (1 - evaporation_rate)

        for tour, tour_length in zip(all_tours, all_lengths):
            for i in range(n-1):
                pheromones[tour[i]][tour[i+1]] += 1 / tour_length
            pheromones[tour[-1]][tour[0]] += 1 / tour_length

    return best_tour, best_length

def display_path(points, tour, iteration, length):
    plt.clf()
    plt.scatter(*zip(*points), marker='o', color='blue')
    for i in range(len(tour)):
        start = points[tour[i-1]]
        end = points[tour[i]]
        plt.plot([start[0], end[0]], [start[1], end[1]], 'k-')
    plt.title(f'Iteration {iteration + 1} - Longueur : {length}')
    plt.pause(0.1)

# Génération aléatoire de points
n_points = 1000
points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n_points)]

# Exécution de l'algorithme d'optimisation par colonies de fourmis
best_tour, best_length = ant_colony_optimization(points)

print("Meilleur tour:", best_tour)
print("Longueur du meilleur tour:", best_length)

# Affichage du meilleur tour
display_path(points, best_tour, -1, best_length)
plt.show()
