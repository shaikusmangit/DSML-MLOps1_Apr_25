import itertools

def dummy_tsp(distance_matrix):
    """
    Dummy TSP solver using brute-force.
    distance_matrix: 2D list representing distances between cities
    Returns the shortest route and its total distance
    """
    n = len(distance_matrix)
    cities = list(range(n))
    min_route = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities[1:]):  # Fix city[0] as starting point
        route = [0] + list(perm) + [0]  # start and end at city 0
        distance = 0
        for i in range(len(route) - 1):
            distance += distance_matrix[route[i]][route[i + 1]]

        if distance < min_distance:
            min_distance = distance
            min_route = route

    return min_route, min_distance
