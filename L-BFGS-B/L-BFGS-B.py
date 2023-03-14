import numpy as np
import scipy.optimize as opt

# Générer des coordonnées aléatoires pour les villes
def generate_random_cities_coordinates(num_cities, seed=42):
    np.random.seed(seed)
    cities_coordinates = np.random.rand(num_cities, 2) * 100
    return cities_coordinates

# Créer une matrice de distance entre les villes à partir de leurs coordonnées
def create_distance_matrix(cities_coordinates):
    num_cities = cities_coordinates.shape[0]
    distance_matrix = np.zeros((num_cities, num_cities))

    # Calculer la distance euclidienne entre chaque paire de villes
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = np.linalg.norm(cities_coordinates[i] - cities_coordinates[j])
            distance_matrix[i, j] = distance_matrix[j, i] = distance

    return distance_matrix

# Trouver une solution approximative au problème du voyageur de commerce (TSP) en utilisant l'algorithme L-BFGS-B
def tsp_optimal_solution(distance_matrix):
    num_cities = distance_matrix.shape[0]
    x0 = np.random.permutation(np.arange(1, num_cities))
    
    # Fonction objectif à minimiser (distance totale parcourue)
    def objective_function(x):
        total_distance = 0
        route = np.concatenate(([0], x, [0]))
        for i in range(num_cities):
            total_distance += distance_matrix[int(route[i]), int(route[i+1])]
        return total_distance
    
    # Définir les limites pour les variables d'optimisation
    bounds = [(1, num_cities - 1)] * (num_cities - 1)
    
    # Exécuter l'optimisation avec la méthode L-BFGS-B
    result = opt.minimize(objective_function, x0, method='L-BFGS-B', bounds=bounds)
    
    # Récupérer l'itinéraire optimal et la distance totale
    optimal_route = np.concatenate(([0], result.x.astype(int), [0]))
    optimal_distance = objective_function(result.x)
    
    return optimal_distance, optimal_route

num_cities = 1000
cities_coordinates = generate_random_cities_coordinates(num_cities)
distance_matrix = create_distance_matrix(cities_coordinates)

# Résoudre le problème du TSP pour l'instance générée
optimal_distance, optimal_route = tsp_optimal_solution(distance_matrix)

# Afficher l'itinéraire optimal et la distance totale dans le terminal
print("Itinéraire optimal :")
print(optimal_route)
print("Distance totale :", optimal_distance)
