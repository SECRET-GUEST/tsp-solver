import numpy as np
from scipy.optimize import minimize
import gmaps
from math import radians, sin, cos, sqrt, atan2

# Remplacez cette clé par votre clé API Google Maps
API_KEY = "YOUR_API_KEY"
gmaps.configure(api_key=API_KEY)

# Liste des

# Remplacez cette clé par votre clé API Google Maps
API_KEY = "YOUR_API_KEY"
gmaps.configure(api_key=API_KEY)

# Liste des adresses (remplacez-les par les adresses souhaitées)
coordinates  = [
    (48.859, 2.345),
    (48.860, 2.345),
    (48.861, 2.344),
    (48.862, 2.343),
    (48.863, 2.342),
    (48.864, 2.341),
    (48.864, 2.340),
    (48.864, 2.339),
    (48.863, 2.338),
    (48.862, 2.337),
    (48.861, 2.336),
    (48.860, 2.335),
    (48.859, 2.334),
    (48.858, 2.333),
    (48.857, 2.334),
    (48.856, 2.335),
    (48.855, 2.336),
    (48.854, 2.337),
    (48.853, 2.338),
    (48.852, 2.339),
    (48.851, 2.340),
    (48.850, 2.341),
    (48.850, 2.342),
    (48.850, 2.343),
    (48.851, 2.344),
    (48.852, 2.345),
    (48.853, 2.346),
    (48.854, 2.347),
    (48.855, 2.348),
    (48.856, 2.349),
    (48.857, 2.348),
    (48.858, 2.347),
    (48.859, 2.346),
    (48.860, 2.347),
    (48.861, 2.348),
    (48.862, 2.349),
    (48.863, 2.348),
    (48.864, 2.347),
    (48.864, 2.346),
    (48.864, 2.345),
    (48.864, 2.344),
    (48.863, 2.343),
    (48.862, 2.342),
    (48.861, 2.341),
    (48.860, 2.340),
    (48.859, 2.339),
    (48.859, 2.338),
    (48.859, 2.337),
    (48.859, 2.336),
    (48.859, 2.335),
    (48.859, 2.334),
    (48.859, 2.333),
    (48.859, 2.332),
    (48.859, 2.331),
    (48.859, 2.330),
    (48.860, 2.329),
    (48.861, 2.328),
    (48.862, 2.327),
    (48.863, 2.326),
    (48.864, 2.325),
    (48.865, 2.325),
    (48.866, 2.324),
    (48.867, 2.323),
    (48.868, 2.322),
    (48.869, 2.321),
    (48.870, 2.320),
    (48.871, 2.319),
    (48.872, 2.318),
    (48.873, 2.317),
    (48.874, 2.316),
    (48.875, 2.315),
    (48.876, 2.314),
    (48.877, 2.313),
    (48.878, 2.312),
    (48.879, 2.311),
    (48.880, 2.310),
    (48.881, 2.309),
    (48.882, 2.308),
    (48.883, 2.307),
    (48.884, 2.306),
    (48.885, 2.305),
    (48.886, 2.304),
    (48.887, 2.303),
    (48.888, 2.302),
    (48.889, 2.301),
    (48.890, 2.300),
    (48.891, 2.299),
    (48.892, 2.298),
    (48.893, 2.297),
    (48.894, 2.296),
    (48.895, 2.295),
    (48.896, 2.294),
    (48.897, 2.293),
    (48.898, 2.292),
    (48.899, 2.291),
    (48.900, 2.290)
]

def haversine_distance(coord1, coord2):
    R = 6371  # Rayon de la Terre en kilomètres

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

def create_distance_matrix(coordinates):
    num_locations = len(coordinates)
    distance_matrix = np.zeros((num_locations, num_locations))

    for i in range(num_locations):
        for j in range(num_locations):
            distance_matrix[i, j] = haversine_distance(coordinates[i], coordinates[j])

    return distance_matrix

def tsp_objective_function(route, distance_matrix):
    num_locations = len(distance_matrix)
    indices = np.array(route, dtype=int)
    indices = np.append(indices, indices[0])
    total_distance = np.sum(distance_matrix[indices[:-1], indices[1:]])
    return total_distance

def solve_tsp_l_bfgs_b(distance_matrix):
    num_locations = len(distance_matrix)
    x0 = np.random.permutation(np.arange(1, num_locations))
    bounds = [(1, num_locations - 1) for _ in range(num_locations - 1)]

    result = minimize(tsp_objective_function, x0, args=(distance_matrix,), method='L-BFGS-B', bounds=bounds)

    optimized_route = np.round(result.x).astype(int)
    optimized_route = np.insert(optimized_route, 0, 0)
    optimized_route = np.append(optimized_route, 0)

    return optimized_route

def display_optimal_route_on_map(route, coordinates):
    optimal_route_coordinates = [coordinates[idx] for idx in route]

    fig = gmaps.figure(center=optimal_route_coordinates[0], zoom_level=14)
    layer = gmaps.directions.Directions(optimal_route_coordinates[0], optimal_route_coordinates[-1],
                                         waypoints=optimal_route_coordinates[1:-1],
                                         mode='DRIVING',
                                         optimize_waypoints=True,
                                         api_key=API_KEY)
    fig.add_layer(layer)

    return fig

def save_map_to_html(fig, filename):
    with open(filename, "w") as f:
        f.write(fig.to_html())


distance_matrix = create_distance_matrix(coordinates)
optimal_route = solve_tsp_l_bfgs_b(distance_matrix)

print("Optimal route (indices):")
print(optimal_route)

print("Optimal route (coordinates):")
for idx in optimal_route:
    print(coordinates[idx])

# Afficher la route optimale sur une carte Google Maps
fig = display_optimal_route_on_map(optimal_route, coordinates)
save_map_to_html(fig, "map.html")